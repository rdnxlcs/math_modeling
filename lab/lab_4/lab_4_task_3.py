# 1 - Собирающая, 0 - Рассеивающая
def opt(type, d, f):
  if type:
    if d < f:
      return(['ув', 'пр', 'мн'])
    elif d == f:
      return('изображение отсутствует')
    elif d > f and d < 2 * f:
      return(['ув', 'пе', 'де'])
    elif d == 2 * f:
      return(['равное', 'пе', 'де'])
    elif d > 2 * f:
      return(['ум', 'пе', 'де'])
  else:
    return(['ум', 'пр', 'мн'])
type, d, f = map(int, input().split())
print(opt(type, d, f))
    
  