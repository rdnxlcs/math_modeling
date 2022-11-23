import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')

def circle_move(k, v, t):
    a = np.arange(0, t * v, 0.1) 
    x = a
    y = k * np.sin(a)
    return x, y

def h(k, v, t):
    a = np.arange(0, t * v, 0.1) 
    x = a
    y = k * np.tan(a)
    return x, y

edge = 20

ax.set_ylim(-edge, edge)
ax.set_xlim(0, edge)
plt.axis('equal')

def animate(i):
    sin1.set_data(circle_move(2, 0.1, i))
    sin2.set_data(h(2, 0.1, i))
    
ani = FuncAnimation(fig, animate, frames=200, interval=30)

ani.save('ani.gif')