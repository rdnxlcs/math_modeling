import matplotlib.pyplot as plt
import numpy as np

def parabola(xa, xb, n, a, b, c):
  x = np.arange(xa, xb, n)
  y = a*x**2 + b*x + c
  plt.plot(x, y, color='r', label='parabola')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'parabola'
  plt.show()

def gyperbola(xa, xb, n, k):
  x = np.arange(xa, xb, n)
  y = k / x
  plt.plot(x, y, color='b', label='gyperbola')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'gyperbola'
  plt.show()

def gyperbola2(a, b):
  x = np.arange(-100, 100, 0.1)
  y = np.arange(-100, 100, 0.1)
  X, Y = np.meshgrid(x, y)
  f = (X**2/a**2) - (Y**2/b**2)
  plt.contour(X, Y, f, levels = [10])
  plt.show()

  
gyperbola(1, 10, 0.01, 1)