import numpy as np
from math import cos, sin, radians
x0 = 0
y0 = 0
g = 9.8
v0 = float(input("Начальная скорость: "))
a = float(input("Угол: "))
vx = v0 * cos(radians(a)) 
vy = v0 * sin(radians(a)) 
t = np.arange(0, 10, 0.01)
y = vy * t - (g * t ** 2)/2
x = vx * t
