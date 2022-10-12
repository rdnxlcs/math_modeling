n = int(input())
for i in range(1, n): 
  a = []
  for j in range(1, i): 
    if i % j == 0: 
      a.append(j) 
    else: 
      continue 
  if sum(a) == i: 
    print(i) 
  else: 
    continue