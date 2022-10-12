a, b, c = map(int, input().split()) 
if a + b > c and b + c > a and a + c > b: 
  if a == b and a == c: 
    print('equilateral') 
  elif a == b or a == c or b == c:
    print('isosceles') 
  else:
    print('scalene')  
else: print('non-exist')