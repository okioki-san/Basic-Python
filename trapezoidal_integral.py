from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math


def Answer(f, a=0, b=1, n=100):
    h=(b-a)/n
    k=1
    S=0
    while k<=n:
        S+=h/2*(f(a+(k-1)*h)+f(a+k*h))
        k+=1
    return S

def f1(x):
    return sin(x)
def f2(x):
    return 4/(1+x**2)
def f3(x):
    return math.pi**(1/2)*math.exp(-x**2)

result1=Answer(f1, 0, math.pi/2, 50)
result2=Answer(f2)
result3=Answer(f3, -100, 100, 1000)

print("(1)"+str(result1), "(2)"+str(result2), "(3)"+str(result3))