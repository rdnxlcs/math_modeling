a = []
b = []
c = []
def mtrx_inpt(mtrx):
  t = []
  while t != [0]:
    t = list(map(int, input().split()))
    mtrx.append(t)
  del mtrx[-1]
mtrx_inpt(a)
mtrx_inpt(b)
for i in range(len(a)):
  for j in range(len(a[i])):
    if a[i][j] >= b[i][j]:
      c.append(a[i][j])
    else:
      c.append(b[i][j])
print(c)
