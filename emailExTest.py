from emails import EmailSender

server = "server"
sender = "sender@mail.com"
user ="user"
pwd = "pwd"
receivers = ['receiver@mail.com']
subject = "subject"
message = "message"

mail = EmailSender(server, user, pwd)
mail.send_text_email(sender, receivers, subject, message)