for i in range(1, 10):
  a = []
  for j in range(1, 10):
    a.append(j * i)
  print(" ".join(map(str, a)))