import math
def f(g, H):
    return math.sqrt(2 * g * H)
g = 9.81
H = 1000
v0 = f(g, H)
print("{:.2f}".format(v0))