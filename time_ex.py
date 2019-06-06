from datetime import datetime, date, timedelta, timezone
import pytz


class DateOperator:
	@staticmethod
	def last_month_day(now_time):
		last_month = now_time.month - 1
		last_year = now_time.year

		if last_month == 0:
			last_month = 12
			last_year -= 1

		month_day = date(month=last_month, year=last_year, day=1)
		return month_day

	@staticmethod
	def last_week_day(now_time):
		now = now_time
		if isinstance(now_time, datetime):
			now = now_time.date()

		day_diff = now.weekday() + 7
		one_week = timedelta(days=day_diff)

		return now - one_week

	@staticmethod
	def yesterday(now_time):
		now = now_time
		if isinstance(now_time, datetime):
			now = now_time.date()

		one_day = timedelta(days=1)
		return now - one_day

	@staticmethod
	def tomorrow(now_time):
		now = now_time
		if isinstance(now_time, datetime):
			now = now_time.date()

		one_day = timedelta(days=1)
		return now + one_day

	@staticmethod
	def to_utc(naive_time, tz_name):
		date_time = None
		timezone = pytz.timezone(tz_name)

		if isinstance(naive_time, date):
			date_time = datetime(naive_time.year, naive_time.month, naive_time.day)
		elif isinstance(naive_time, datetime):
			date_time = naive_time
		else:
			return

		if date_time.tzinfo is None:
			dt_local = timezone.localize(date_time)
		else:
			dt_local = date_time

		return dt_local.astimezone(pytz.utc)

	@staticmethod
	def convert_timezone(naive_time, from_tzname, to_tzname):
		date_time = None
		from_timezone = pytz.timezone(from_tzname)
		to_timezone = pytz.timezone(to_tzname)

		if isinstance(naive_time, datetime):
			date_time = naive_time
		elif isinstance(naive_time, date):
			date_time = datetime(naive_time.year, naive_time.month, naive_time.day)
		else:
			return

		if date_time.tzinfo is None:
			dt_from = from_timezone.localize(date_time)
		else:
			dt_from = date_time

		return dt_from.astimezone(to_timezone)

	@staticmethod
	def strformat(naive_time):	
		date_string = datetime.strftime(naive_time, '%m/%d/%Y')		
		return date_string

	@staticmethod
	def isoformat(naive_time):	
		return naive_time.isoformat()		

	@staticmethod
	def current_timezone():	
		now = datetime.now(timezone.utc).astimezone()
		return now.isoformat()