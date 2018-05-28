from timeEx import DateOperator
from datetime import datetime as dt

now_time = dt.now() 

last_month_day = DateOperator.last_month_day(now_time)
last_week_day = DateOperator.last_week_day(now_time)
yesterday = DateOperator.yesterday(now_time)
tomorrow = DateOperator.tomorrow(now_time)

utc_time = DateOperator.to_utc(now_time, 'UTC')

convert_timezone = DateOperator.convert_timezone(now_time,'Asia/Taipei', 'Asia/Tokyo')

strformat = DateOperator.strformat(now_time)

isoformat = DateOperator.isoformat(now_time)

current_timezone = DateOperator.current_timezone()

print(last_month_day)
print(last_week_day)
print(yesterday)
print(tomorrow)
print(utc_time)
print(convert_timezone)
print(strformat)
print(isoformat)
print(current_timezone)