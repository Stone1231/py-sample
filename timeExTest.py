from timeEx import DateOperator
from datetime import datetime, timedelta

now_time = datetime.now() 

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

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8, minutes=20)
gen = (once_upon_a_time + x * delta for x in range(5))
print(type(gen)) # generator
print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))

# 時間差
delta_min = timedelta(minutes=10)
some_time = now_time + timedelta(minutes=11)
is_delta = (some_time - now_time) > delta_min
print(is_delta)