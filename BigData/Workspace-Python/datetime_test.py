import datetime as dt
now =dt.datetime.now()
cal = "{}-{}, {}".format(now.month, now.day, now.year)
print(cal)

