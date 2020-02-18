# insertion sort

class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre
    
  def __str__(self):
    return f'{self.genre}: {self.title} by {self.author}'
  
  
b1 = Book('Food for thought', 'John Jones', 'Food')
b2 = Book('My life in reality', 'Don Davis', 'Life')
b3 = Book('Apples, how you like them?', 'Stan Simpson', 'Food')
b4 = Book('Just Do It', 'Shia Le Boeuf', 'Inspirational')
b5 = Book('What is this code anyway', 'Tom Jones', 'Programming')


books = [b1, b2, b3, b4, b5]

def in_sort(books):
  # loop through length -1 elements
  for i in range(1, len(books)):
    
    # code up some logic
    # save current i to a temp variable
    temp = books[i]
    j = i
    
    while j > 0 and temp.title < books[j - 1].title:
      # shift left until correct title is found
      books[j] = books[j - 1]
      j -= 1
    # insert book in correct position
    books[j] = temp   
    
  return books

for b in books:
  print(b)
  print('----------')

in_sort(books)

for b in books:
  print(b)

