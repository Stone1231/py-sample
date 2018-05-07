from datetime import datetime as dt, timedelta,timezone

today = dt.now() 
date_string = dt.strftime(today, '%m/%d/%Y') 
print(date_string)

now_bef_10 = today + timedelta(minutes = -10) #十分鐘前
print(now_bef_10)

print(now_bef_10.isoformat())

print(now_bef_10(timezone.utc).astimezone().isoformat()) #顯示時區