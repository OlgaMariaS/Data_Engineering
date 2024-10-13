from datetime import timedelta, date, time, datetime

date = datetime(2024,10,8,17,30)

date = date + timedelta(weeks=1)
print(date)

# Take a current day and hour
now = datetime.now()
one_hour = 1 

now_more_hour = now + timedelta(hours=one_hour)
print(now_more_hour)

# Another way
now_minius = now + timedelta(minutes=30)
print(now_minius.time())
