class Bicycle():
  def exclaim(self):
    print("I'm a bicycle!")
    
class Specialized(Bicycle):
  # this new method underneath supercedes the parent method
  def exclaim(self):
    print("I'm a Specialized Bicycle!")
  pass

a_bicycle = Bicycle()
a_specialized = Specialized()

a_bicycle.exclaim()
a_specialized.exclaim()

class Student():
  def __init__(self, name):
    self.name = name
    
class Graduate(Student):
  def __init__(self, name, graduation_date):
    # to access the parent method of the same name, we use super.  It takes over the method in the child class of the same name.
    super().__init__(name)
    self.graduation_date = graduation_date
    
john_lennon = Graduate("John Lennon", "8th December 1980")
print(john_lennon.name)
print(john_lennon.graduation_date)

# CHALLENGE

class Aunty:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return(f"Hello my name is {self.name} and I am {self.age} years old.")
  
class Nephew(Aunty):
  def __init__(self, name, age, fave_toy):
    super().__init__(name, age)
    self.fave_toy = fave_toy
  def __str__(self):
    return(f"Hello I'm a wee boy.  My name is {self.name} I'm {self.age} and 1/2 years old.  My fave toy is {self.fave_toy}.")
  def lego(self):
    return (f"I'm going to play with my {self.fave_toy} right now!!!")
  
class Niece(Aunty):
  def __init__(self, name, age, fave_food):
    super().__init__(name, age)
    self.fave_food = fave_food
  def __str__(self):
    return(f"Hello I'm a wee girl.  My name is {self.name} I'm {self.age} and 1/4 years old.  My fave food is {self.fave_food}.")
  def eat(self):
    return (f"I'm going to eat my {self.fave_food} right now!!! YUM!!")
  
jayne = Aunty("Jayne", 21)
print(jayne)

riley = Nephew("Riley", 4, "Lego")
print(riley)
print(riley.name)
print(riley.lego())

macey = Niece("Macey", 4, "Chips")
print(macey)
print(macey.eat())