import numpy as np
print("Size")
x, y = map(int, input().split())
a = np.zeros((x, y))
b = np.zeros((x, y))
c = np.zeros((x, y))
print("A")
for i in range(x):
  t = list(map(int, input().split()))
  for j in range(y):
    a[i, j] = t[j]
print("B")
for i in range(x):
  t = list(map(int, input().split()))
  for j in range(y):
    b[i, j] = t[j]
    c[i, j] = max(a[i, j], b[i, j])
print(c)


