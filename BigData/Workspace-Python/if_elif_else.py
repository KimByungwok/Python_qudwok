import datetime as dt

now = dt.datetime.now()
month = now.month

if 3<= month <=5:
    print("{}월은 봄입니다.".format(month))
elif month <=8: # 6<=month<=8
    print("{}월은 여름입니다.".format(month))
elif month <=11:
    print("{}월은 가을입니다.".format(month))    
else:
    print("{}월은 겨울입니다.".format(month))    
