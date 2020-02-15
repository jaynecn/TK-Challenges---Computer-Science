

## print the rules of the game
print('Choose a number between 1 and 10, and I will guess it')
print('You have to tell me if my guess greater than or equal to your number')


# set a sentinal value to exit loop
correct = False
# set the top and bottom bounds
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_number = 1

# REPL
# continue looping until a condition is false
while not correct:
  ## have the computer guess the number
  computer_guess = start_number
  
  
  ## take input from user
  print(f'I am guessing it is {computer_guess}')
  result = input('is it Greater, or Equal? ')[0].lower()
  
  result = result[0]
  
  ## evaluate input
  if result == 'g':
    start_number = computer_guess + 1
  elif result == 'e':
    print(f'\nIt is {computer_guess}!\n')
    print(f'Thank you for playing')
    correct = True
    
  if start_number > numbers[9]:
    print(f'Your number has to be less than 10! Start the game over again!!')
    correct = True
    
  else:
    print('Please enter either greater or equal')
