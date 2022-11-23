import numpy as np
print("Size")
x, y = map(int, input().split())
a = np.zeros((x, y))
b = np.zeros((y, x))
print("A")
for i in range(x):
  t = list(map(int, input().split()))
  for j in range(y):
    a[i, j] = t[j]
    b[j, i] = t[j]
for el in b:
  print(max(el))
      