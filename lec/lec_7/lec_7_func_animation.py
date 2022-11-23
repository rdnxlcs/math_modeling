import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-8, 8)
ax.set_ylim(0, 64)

def update(frame):
    xdata.append(frame)
    ydata.append((frame)**2)
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, update, frames=np.arange(-8, 8, 0.1), interval=50)

ani.save('ani.gif')