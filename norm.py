import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as plt3d
from test import generate, genmass

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 2
t = np.linspace(0, 10, 1000)

def matrix(z, cols):
	rows = int(len(z) / cols)
	d = np.array(z).reshape(rows, cols)
	d = list(map(list, d))
	return d
  


def betweens(get, m, q, mainPIdx):
   mainP = get[mainPIdx]

   Fx = []
   Fy = []
   Fz = []
   for i in range(len(get)):
      if i != mainPIdx:
         currentP = get[i]
         r = (mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2 + (mainP[4] - currentP[4])**2
            
         Fx.append((k * q[mainPIdx] * q[i] * (mainP[0] - currentP[0])) / (r ** (3/2) *  m[mainPIdx]))
         Fy.append((k * q[mainPIdx] * q[i] * (mainP[2] - currentP[2])) / (r ** (3/2) *  m[mainPIdx]))
         Fz.append((k * q[mainPIdx] * q[i] * (mainP[4] - currentP[4])) / (r ** (3/2) *  m[mainPIdx]))     

         Fx.append((-G * m[i] * (mainP[0] - currentP[0])) / r ** (3/2))
         Fy.append((-G * m[i] * (mainP[2] - currentP[2])) / r ** (3/2))
         Fz.append((-G * m[i] * (mainP[4] - currentP[4])) / r ** (3/2))

   return (sum(Fx)), (sum(Fy)), (sum(Fz))

# Определяем функцию для системы диф. уравнений
def move_func(s, t):

   get = matrix(list(s), 6)
   
   res = []
   print(t/seconds_in_year)
   for i in range(len(get)):
         
      axe, aye, aze = betweens(get, m, q, i)
      res.append(get[i][1]) #dxdt
      res.append(axe) #dvxdt
      res.append(get[i][3]) #dydt
      res.append(aye) #dvydt
      res.append(get[i][5]) #dzdt
      res.append(aze) #dvzdt

   return tuple(res)

# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений
AE = 149 * 10**9

s0 = (0, 0, 0, 0, 3, 0,
      2, 0, 0, 10, 0, 0,
      -2, 0, 0, 6, -4, 0)


m = [0.01, 0.1, 0.02]
q = [6 * 10**-5, -10**-5, 10**-5]

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

count = 3

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)

# Строим решение в виде графика и анимируем
fig = plt.figure()
ax = plt3d.Axes3D(fig)
fig.add_axes(ax)

balls = []
balls_lines = []

colors = ['r', 'b', 'r']

for i in range(count):
    balls.append(plt.plot([], [], 'o', color = colors[i]))
    balls_lines.append(plt.plot([], [], '-', color = colors[i]))

def animate(i):
   print(round(i / (frames / 100), 1), '%')
   for j in range(count):
        balls[j][0].set_data(sol[i, 6*j], sol[i, 6*j+2])
        balls[j][0].set_3d_properties(sol[i, 6*j+4])

        balls_lines[j][0].set_data(sol[:i, 6*j], sol[:i, 6*j+2])
        balls_lines[j][0].set_3d_properties(sol[:i, 6*j+4])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')

LY = 9.4 * 10**15


edge = 10
ax.set_xlim3d([-edge, edge])
ax.set_xlabel('x')
ax.set_ylim3d([-edge, edge])
ax.set_ylabel('y')
ax.set_zlim3d([-edge, edge])
ax.set_zlabel('z')


ani.save('norm.gif')