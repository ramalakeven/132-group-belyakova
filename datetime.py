import datetime

x = datetime.datetime.now()
daynow = x.strftime("%j")
leapyeardays = (int(x.strftime("%y")) - 3)//4      
daysbefore = (int(x.strftime("%y")) - 2)*365 + leapyeardays + (365 - int((datetime.datetime(2001,7,9)).strftime("%j")))
print(int(daynow)+int(daysbefore))