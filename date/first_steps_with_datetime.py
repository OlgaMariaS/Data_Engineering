# Module import datetime 
from datetime import datetime, date, time

# Date          yyyy-mm-dd
birthday = date(2024,9,14)
print(birthday)

# Time      hh- mm- ss
hour = time(16, 30, 15)
print(hour)

# Date and time 
birth = datetime(2024,9,14, 00, 30, 18)
print(birth)

# constructor, can be used datetime.today()
print(date.today()) 
