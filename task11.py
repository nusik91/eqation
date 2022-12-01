# Дана функция f(x) = -12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30

# 1 Опоределить корни
from sympy import *
import math
import matplotlib.pyplot as plt

x,y,z = symbols('x y z')

func=(-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30)

y=solve(func)
x1=float(y[0])
x2=float(y[1])
print(x1,x2)

# 2 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))

# 3 Найти интервалы, на которых функция убывает

print(solve(fd<0))

# 4 Построить график


list_y=[]
for i in range(-2,3):
    x=i
    y=-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30
    list_y.append(y)
print(list_y)
plt.plot(range(-2,3),[0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-2,3),list_y)
print(func)

# 5 Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=-12*x**4*math.sin(math.cos(x))-18*x**3+5*x**2+10*x-30
print(top,y)

# 6 Определить промежутки, на котором f > 0

solve(0<func)

# 7 Определить промежутки, на котором f < 0

solve(func<0)