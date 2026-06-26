from  datetime import date,datetime,timedelta

dt=datetime.now()
print(date.today())
# print(dt.month,dt.hour,dt.min,dt.date)
print(dt.strftime("%d-%Y-%m %B %H:%M:%S %p"))

date_string = "26-06-2026"
d = datetime.strptime(date_string, "%d-%m-%Y")
future= d + timedelta(days=10)
print(future)
print(d)

d1=date(2026,7,15)
d2=date(2026,6,26)
diff = d1-d2
print(diff)

now = datetime.now()
print(now.timestamp())

