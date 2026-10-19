import math

a = float(input())
b = float(input())
h = float(input())

x = a
while x <= b:
    if x < 0:
        z = x**3
    elif x > 0 and x <= 1:
        z = math.cos(x)
    else:
        z = math.tan(x)
    print(x, z)
    x = x + h