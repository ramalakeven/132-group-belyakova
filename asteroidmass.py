import math
from datetime import datetime, timedelta

date1 = (input("Введите дату рождения:   "))
date = datetime.strptime(date1, '%d.%m.%Y')
m1 = (datetime.strptime("01.09.2003", '%d.%m.%Y') -  date)
m1 = float(m1.days) * 1000
r = math.pow(10,8)
G = 6.676  *  math.pow(10,-11)
m2 = 5.976   *  math.pow(10,24)
F = (G * m1 * m2 )/ (math.pow(r,2))

print(F, "Н")