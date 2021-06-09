import math

equation = input("Enter an equation: ")
a = input("Enter lower index: ")
b = input("Enter upper index: ")
n = input("Enter number of rectangles: ")

equation = str(equation)
a = float(a)
b = float(b)
n = int(n)

areaL = 0.0
areaR = 0.0
areaM = 0.0

xChange = ((b - a) / n)

for i in range(n):
    areaL += float(eval(equation.replace("x", str(a + xChange * i))))
areaL *= xChange

for i in range(1, n + 1):
    areaR += float(eval(equation.replace("x", str(a + xChange * i))))
areaR *= xChange

xn = a
for i in range(n):
    areaM += float(eval(equation.replace("x", str((xn + xn + xChange) / 2))))
    xn += xChange
areaM *= xChange

print()
print("Ln = " + str(round(areaL, 4)))
print("Rn = " + str(round(areaR, 4)))
print("Mn = " + str(round(areaM, 4)))
