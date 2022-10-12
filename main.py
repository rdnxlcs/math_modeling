def exp(a, n):
  c = a
  for i in range(n-2):
    c = c * a
    print(c)
  return(a)
a, n = map(int, input().split())
print(exp(a, n))