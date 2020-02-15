

## print the rules of the game
print('Think of any letter in the alphabet, and I will guess it')
print('You have to tell me if my guess is lower, higher or equal to its position in the alphabet eg. a = 1, b = 2, etc.')


# set a sentinal value to exit loop
correct = False
# set the left and right bounds
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# left = int(alphabet.index('a'))
# right = int(alphabet.index('z'))
left = 0
right = 25
  
# REPL
# continue looping until a condition is false
while not correct:
  ## have the computer guess the number
    
  guess_letter = alphabet[(int(left + right / 2))]
  guess_number = alphabet.index(guess_letter)
  
  
  
  ## take input from user
  print(f'I am guessing it is {guess_letter}')
  result = input('Lower, Higher, or Equal in the Alphabet? ')[0].lower()
  
  result = result[0]
  
  ## evaluate input
  if result == 'l':
    right = guess_number - 1
    
  elif result == 'h':
    left = guess_number + 1
    
  elif result == 'e':
    print(f'\nIt is {guess_letter}!\n')
    print(f'Thank you for playing')
    correct = True
    
  else:
    print('***Please enter either lower, higher, or equal***')
    
  if left > 25:
    print(f'Your letter has to be in the Alphabet! Start the game over again!!')
    correct = True
        
  if left == right:
    guess = left
    print(f'\nIt must be {guess}!\n')
    print(f'Thank you for playing')
    correct = True
    
  
  
  ## print result
