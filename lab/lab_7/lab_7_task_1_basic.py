import matplotlib.pyplot as plt
import numpy as np

def astroid(R):
  t = np.arange(-100, 100, 0.1)
  x = R * np.cos(t)**3
  y = R * np.sin(t)**3
  plt.plot(x, y, color='b', label='astroid')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'astroid'
  plt.axis('equal')
  plt.show()
  
def cilcoid(R):
  t = np.arange(-100, 100, 0.1)
  x = R * (t - np.sin(t))
  y = R * (1 - np.cos(t))
  plt.plot(x, y, color='b', label='cilcoid')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.title = 'cilcoid'
  plt.axis('equal')
  plt.show()

cilcoid(10)
