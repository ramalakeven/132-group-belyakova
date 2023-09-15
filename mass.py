import math, datetime

m1 = float(input("Введите массу объекта деленную на 10^22:   ")) *math.pow(10,22)

r = float(input("Введите расстояние до объекта в километрах:   ")) *1000

G = 6.676  *  math.pow(10,-11)
m2 = 5.976   *  math.pow(10,24)
F = (G * m1 * m2 )/ (math.pow(r,2) * math.pow(10,20))
print(F, "* 10^20 Н")

