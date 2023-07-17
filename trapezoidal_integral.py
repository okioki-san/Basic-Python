from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

a = 0
b = math.pi/2
n=100
h=(b-a)/n
k=1
S=0
while k<=n:
    S+=h/2*(sin(a+(k-1)*h)+sin(a+k*h))
    k+=1
print(S)