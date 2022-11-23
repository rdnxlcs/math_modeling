import matplotlib.pyplot as plt
import numpy as np

def func(a, b):
  x = np.arange(-10, 10, 0.01)
  y = []
  for p in x:
    if p < a:
      y.append(a**2)
    elif p >= a and p <= b:
      y.append(p**2)
    elif p > b:
      y.append(b**2)
      
  plt.plot(x, y, color='g', label='pieces')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.show()

func(1, 5)