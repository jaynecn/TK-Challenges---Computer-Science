def basicRecursion(max, current):
  if (current > max):
    return
  print(f'current: {current}')
  basicRecursion(max, current+1)

basicRecursion(6, 1)
 
def fibonacci(n):
  if n == 0: # base case
    return 0
  if n == 1: # base case
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

# def factorial (n):
#   if ( n < 2 ):
#     return 1
#   return n * factorial(n - 1)

# print(factorial(5))