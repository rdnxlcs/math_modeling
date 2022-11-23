import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

def butterfly(t):
    xdata.append(np.sin(t)*(np.e**np.cos(t)-2 * np.cos(4 * t) + np.sin(t / 12)**5))
    ydata.append(np.cos(t)*(np.e**np.cos(t)-2 * np.cos(4 * t) + np.sin(t / 12)**5))
    anim_object.set_data(xdata, ydata)
    return anim_object,

def heart(t):
    xdata.append(16 * np.sin(t)**3)
    ydata.append(13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))
    anim_object.set_data(xdata, ydata)
    return anim_object,

def star(t):
    xdata.append(12 * np.cos(t) + 8 * np.cos(1.5 * t))
    ydata.append(12 * np.sin(t) - 8 * np.sin(1.5 * t))
    anim_object.set_data(xdata, ydata)
    return anim_object,


ani = FuncAnimation(fig, star, frames=np.arange(0, 4*np.pi, 0.1), interval=50)

ani.save('ani.gif')
