# install pip install pytz

import datetime
import pytz

# Time zone from São Paulo 
date = datetime.datetime.now(pytz.timezone("America/Sao_paulo"))
print(date)

#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones