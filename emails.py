#!/usr/bin/env python3

import smtplib
import re
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header


class EmailSender:
	""" A helper class that encapsulate email send functions. """
	def __init__(self, server, user="", password="", port=25, anonymous=False):
		self.smtp_user = user
		self.smtp_password = password
		self.smtp_server = server
		self.smtp_port = port
		self.anonymous = anonymous

	@staticmethod
	def check_sender(sender):
		if not sender:
			return False
		elif not isinstance(sender, str):
			return False
		elif not EmailSender.check_email_address(sender):
			return False
		else:
			return True

	@staticmethod
	def check_receivers(receivers):
		if not receivers:
			return False
		elif not isinstance(receivers, (list, tuple)):
			return False

		passed = True
		for receiver in receivers:
			if not EmailSender.check_email_address(receiver):
				passed = False
				break

		return passed

	@staticmethod
	def check_ccs(ccs):
		if not ccs:
			return True
		elif not isinstance(ccs, (list, tuple)):
			return False

		passed = True
		for cc in ccs:
			if not EmailSender.check_email_address(cc):
				passed = False
				break

		return passed

	@staticmethod
	def check_subject(subject):
		if not subject:
			return False
		elif not isinstance(subject, str):
			return False
		else:
			return True

	@staticmethod
	def check_message(message):
		if not message:
			return False
		elif not isinstance(message, str):
			return False
		else:
			return True

	@staticmethod
	def check_MIME(message):
		if not message:
			return False
		elif not isinstance(message, (MIMEText, MIMEMultipart)):
			return False
		else:
			return True

	@staticmethod
	def check_attachment(files):
		if not files:
			return True
		elif not isinstance(files, (list, tuple)):
			return False

		passed = True
		for file in files:
			if not isinstance(file, str):
				passed = False
				break
			elif not os.path.exists(file):
				passed = False
				break

		return passed

	@staticmethod
	def check_email_address(address):
		if not address:
			return False
		elif not isinstance(address, str):
			return False

		email_pattern = r"^[a-zA-Z0-9_\.+\-]+(@|(%40))[a-zA-Z0-9]+\.[a-zA-Z0-9\.]+$"
		return bool(re.search(email_pattern, address))

	@staticmethod
	def check_email_parameters(sender, receivers, subject, ccs=None, message=None, attachments=None, skip_message=True):
		result_info = {"code": 0, "message": ""}
		if not EmailSender.check_sender(sender):
			result_info["code"] = -1
			result_info["message"] = "Invalid sender."
			return result_info

		if not EmailSender.check_receivers(receivers):
			result_info["code"] = -2
			result_info["message"] = "Invalid receivers."
			return result_info

		if not EmailSender.check_ccs(ccs):
			result_info["code"] = -3
			result_info["message"] = "Invalid ccs."
			return result_info

		if not EmailSender.check_subject(subject):
			result_info["code"] = -4
			result_info["message"] = "Invalid subject."
			return result_info

		if not skip_message and not EmailSender.check_message(message):
			result_info["code"] = -5
			result_info["message"] = "Invalid message."
			return result_info

		if not EmailSender.check_attachment(attachments):
			result_info["code"] = -6
			result_info["message"] = "Invalid attachments."
			return result_info

		return result_info

	def _send_email(self, sender: str, receivers: list, ccs: list, subject: str, message, sender_description=None) -> dict:
		"""
		Send email help method using smtplib.
		:param sender: Sender's email address
		:param receivers: A list of receiver's email address
		:param subject: The subject of email
		:param message: The body of email, include text or html, and attachments.
		:return: The operate result, True(Success) or False(Failure).
		"""
		result_info = EmailSender.check_email_parameters(sender, receivers, subject)
		if result_info["code"] < 0:
			return result_info

		if not EmailSender.check_MIME(message):
			result_info["code"] = -100
			result_info["message"] = "Invalid MIME."
			return result_info

		message["Subject"] = Header(subject, "utf-8")
		if sender_description:
			message["From"] = Header(sender_description, "utf-8")
		else:
			message["From"] = Header(sender, "utf-8")

		message["To"] = ",".join(receivers)
		combos = receivers[:]

		if ccs:
			message["Cc"] = ",".join(ccs)
			combos += ccs[:]

		try:
			smtp_obj = smtplib.SMTP()
			smtp_obj.connect(self.smtp_server, self.smtp_port)
			if not self.anonymous:
				smtp_obj.login(self.smtp_user, self.smtp_password)
			smtp_obj.sendmail(sender, combos, message.as_string())
			smtp_obj.quit()
		except smtplib.SMTPException as ex:
			result_info["code"] = -7
			result_info["message"] = "Internal Error: {0!r}".format(ex)

		return result_info

	def send_text_email(self, sender, receivers, subject, message, ccs=None, attachments=None, sender_description=None):
		""" Send plain text email with or without attachments. """
		result_info = EmailSender.check_email_parameters(sender, receivers, subject, ccs=ccs, message=message,
														attachments=attachments, skip_message=False)
		if result_info["code"] < 0:
			return result_info

		if attachments:
			msg = MIMEMultipart()

			msg.attach(MIMEText(message, "plain", "utf-8"))

			if EmailSender.check_attachment(attachments):
				for attachment in attachments:
					file_name = os.path.split(attachment)[-1]
					try:
						file = open(attachment, 'rb')
						buffer = file.read()
						file.close()
					except:
						result_info["code"] = -8
						result_info["message"] = "Cannot open file: " + attachment
						return result_info

					att = MIMEApplication(buffer)
					# att["Content-Type"] = "application/octet-stream"
					att["Content-Disposition"] = "attachment;filename={0}".format(file_name)
					msg.attach(att)
		else:
			msg = MIMEText(message, "plain", "utf-8")

		return self._send_email(sender, receivers, ccs, subject, msg, sender_description)

	def send_html_email(self, sender, receivers, subject, message, ccs=None, attachments=None, sender_description=None):
		""" Send html email with or without attachments. """
		result_info = EmailSender.check_email_parameters(sender, receivers, subject, ccs=ccs, message=message,
														attachments=attachments, skip_message=False)
		if result_info["code"] < 0:
			return result_info

		if attachments:
			msg = MIMEMultipart()
			# msg["Subject"] = Header(subject, "utf-8")
			# if sender_description:
			#	msg["From"] = Header(sender_description, "utf-8")

			msg.attach(MIMEText(message, "html", "utf-8"))

			if EmailSender.check_attachment(attachments):
				for attachment in attachments:
					index = attachment.rfind('/')

					file_name = os.path.split(attachment)[1]

					file = open(attachment, 'rb')
					buffer = file.read()
					file.close()

					# att = MIMEText(buffer, "base64", "utf-8")
					att = MIMEApplication(buffer)
					# att["Content-Type"] = "application/octet-stream"
					att["Content-Disposition"] = "attachment;filename={0}".format(file_name)
					msg.attach(att)
		else:
			msg = MIMEText(message, "html", "utf-8")

		return self._send_email(sender, receivers, ccs, subject, msg, sender_description)
