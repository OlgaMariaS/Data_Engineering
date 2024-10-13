import datetime
# Python is permited converte date and time for formatation 

# Methods are:
# strftime (string format time)
# strptime (string Parse time)

# Formatting date and time for bralizian patters 
current_date = datetime.datetime.now()
print(current_date.strftime("%d/%m/%Y as %H:%M"))

# Convertion of string in date 
string = "13/10/2024 as 11:50"
date = datetime.datetime.strptime(string, "%d/%m/%Y as %H:%M")
print(date)