def mtrx_inpt(mtrx):
  t = []
  while t != [0]:
    t = list(map(int, input().split()))
    mtrx.append(t)
  del mtrx[-1]
a = []
mtrx_inpt(a)
for i in range(len(a[0])):
  t = []
  for j in range(len(a)):
    t.append(a[j][i])
  print(max(t))
