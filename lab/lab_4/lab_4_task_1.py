def exp(a, n):
  c = a
  for i in range(n-1):
    c = c * a
  return(c)
a, n = map(int, input().split())
print(exp(a, n))