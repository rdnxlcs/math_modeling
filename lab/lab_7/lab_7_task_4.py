import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], '-', color='r')

def circle_move(vr, t):
    a = np.arange(0, 4 * np.pi, 0.1)
    x0 = [-5, 5, 5, -5]
    y0 = [5, 5, -5, -5]
    x = x0 * np.cos(vr * t) - y0 * np.sin(vr * t)
    y = x0 * np.sin(vr * t) + y0 * np.cos(vr * t)
    return x, y
edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(0.1, i))
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('ani.gif')
