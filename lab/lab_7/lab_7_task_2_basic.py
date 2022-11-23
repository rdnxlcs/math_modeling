import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], '--', color='r')

xdata, ydata = [], []


def circle_move(vr, t):
  R = vr * t
  alpha = np.arange(0, 2 * np.pi, 0.1)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y


edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
  ball.set_data(circle_move(0.1, i))


ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('ani.gif')
