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

# Lists #
colours = ['red', 'green', 'yellow']
colours[0] = 'blue'
print(colours)
for i in range(0, len(colours)):
  print(colours[i])
print(colours.index('blue', 0))
print(len(colours))
colours.append('orange')
print(colours)
colours.insert(2, 'pink')
print(colours)
colours.remove('pink')
print(colours)
del colours[0]
print(colours)

vowel_string = 'aeiou'
print(list(vowel_string))

# Dictionaries #
jayne = {"name": "Jayne", "age": 21, "year": 2020, "rich": "Nope"}
jayne["rich"] = "yes"
print(jayne)
# print dictionary keys line by line #
for key in jayne.keys():
  print(key)

# print dictionary values line by line #
for value in jayne.values():
  print(value)
  
print(jayne.values())

# check index of an entry in dictionary #
print("name" in jayne)
print(len(jayne))

# add item to dictionary #
jayne["tired"] = "yes"
print(jayne)
jayne.pop("tired")
print(jayne)
jayne.clear()
print(jayne)