def basicRecursion(max, current):
  if (current > max):
    return
  print(f'current: {current}')
  basicRecursion(max, current+1)

basicRecursion(6, 1)