import matplotlib.pyplot as plt
from math import floor
import numpy as np

def func():
  x = np.arange(-10, 10, 0.01)
  y = []
  for p in x:
    n = floor(p)
    y.append(n)
      
  plt.plot(x, y, color='g', label='pieces')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.show()

func()