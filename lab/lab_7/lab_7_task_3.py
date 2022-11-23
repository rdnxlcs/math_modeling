import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], '-', color='r')

def circle_move(vr, t):
    a = np.arange(0, 4 * np.pi, 0.1)
    x0 = 12 * np.cos(a) + 8 * np.cos(1.5 * a)
    y0 = 12 * np.sin(a) - 8 * np.sin(1.5 * a)
    x = x0 * np.cos(vr * t) - y0 * np.sin(vr * t)
    y = x0 * np.sin(vr * t) + y0 * np.cos(vr * t)
    return x, y
edge = 30
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(0.1, i))
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('ani.gif')
