import matplotlib.pyplot as plt
import numpy as np

def liss(A, B, a, b, s):
  t = np.arange(-100, 100, 0.1)
  x = A * np.sin(a * t + s)
  y = B * np.sin(b * t)
  plt.plot(x, y, color='b', label='liss')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'liss'
  plt.axis('equal')
  plt.show()

liss(1, 2, 0.5, 0.3, np.pi/2)