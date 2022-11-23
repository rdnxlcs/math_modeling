def fib(n):
  t = [0, 1]
  for i in range(abs(n) - 1):
    t.append(sum(t))
    del t[0]
  if n >= 0:
    return(t[-1])
  else:
    return(-(t[-1]))
print(fib(int(input())))