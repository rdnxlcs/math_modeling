from math import sqrt
print(2)
a, b, c = map(int, input().split())
D = b**2 - 4 * a * c
if D > 0:
  print((-b + sqrt(D)) / (2 * a))
  print((-b - sqrt(D)) / (2 * a))
elif D == 0:
  print(-b / (2 * a))
elif D < 0:
  print("D < 0")