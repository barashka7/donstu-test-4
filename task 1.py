import math
x = float(input("число x: "))
n = int(input("число n: "))
res = sum((x**i) / math.factorial(i) for i in range(1, n + 1))
print('Сумма:',res)

