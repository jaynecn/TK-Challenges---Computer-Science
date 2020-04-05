def do_twice(function, value):
    function(value)
    function(value)
    
def print_spam():
    print('spam')
    
def print_twice(arg):
  print(arg)
  print(arg)

do_twice(print_twice, ('boo'))

def do_four(function, value):
  do_twice(function, value)
  do_twice(function, value)
  
# do_four(do_twice(print_twice, ('yaaay')))

def check_fermat(a, b, c, n):
  if(n > 2 and a**n + b**n == c**n):
    print("Holy smokes, Fermat was wrong!")
  else: print("No, that doesnt work")
  
check_fermat(2,3,4,5)
