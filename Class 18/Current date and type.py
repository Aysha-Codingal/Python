from datetime import date,time,datetime

dt = date.today()
print("Todays date is",dt)
t = datetime.now()
print("The current time is",t)

print(dt.day,"-",dt.month,"-",dt.year)
