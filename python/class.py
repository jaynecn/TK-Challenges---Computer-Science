
class MyFirstClass:
  pass

a = MyFirstClass()
print(a)

b = MyFirstClass()
print(b)

class Coder:
  def __init__(self, name, age, language):
    self.name = name
    self.age = age
    self.language = language
  def __str__(self):
    return(f"Hi folks my name is {self.name} I am {self.age} years old and my fave language is {self.language}.")
  def __repr__(self):
    return 'Info: (name=%s, age=%s)' % (self.name, self.age)
  
      
n00b = Coder("Jayne", 21, "Python")
print(n00b)
    
