import matplotlib.pyplot as plt
import numpy as np


def ququ():
  f = np.arange(0, 8 * np.pi, 0.1)
  e = 0.5
  p = 2
  r = p / (1 + e * np.cos(f))
  x = r * np.cos(f)
  y = r * np.sin(f)
  plt.plot(x, y, color='b', label='ququ')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'ququ'
  plt.axis('equal')
  plt.show()


ququ()