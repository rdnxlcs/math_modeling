import matplotlib.pyplot as plt
import numpy as np

def ell(a, b):
  x = np.arange(-50, 50, 0.1)
  y = np.arange(-50, 50, 0.1)
  X, Y = np.meshgrid(x, y)
  f = (X**2/a**2) + (Y**2/b**2)
  plt.contour(X, Y, f, levels = [100])
  plt.show()

def circ(r):
  x = np.arange(-2*r, 2*r, 0.1)
  y = np.arange(-2*r, 2*r, 0.1)
  X, Y = np.meshgrid(x, y)
  f = X**2 + Y**2
  plt.contour(X, Y, f, levels = [r**2])
  plt.axis('equal')
  plt.show()

circ(10)