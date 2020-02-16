arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

left = arr[0]
right = arr[19]


correct = False 

while not correct:
  number = int((left + right) / 2)
  guess = arr[number]
  print(guess)

  print(f'I think your number is {guess}')
  result = input('Is it Higher, Lower, or Equal? ')[0].lower()

  result = result[0]

  if result == 'l':
    right = guess - 1
    
  elif result == 'h':
    left = guess + 1
  
  elif result == 'e':
    print(f'\nIt is {guess}!\n')
    print(f'Thank you for playing')
    correct = True
  
  else:
      print('***Please enter either lower, higher, or equal***')

  if left == right:
      guess = left
      print(f'\nIt must be {guess}!\n')
      print(f'Thank you for playing')
      correct = True
    
