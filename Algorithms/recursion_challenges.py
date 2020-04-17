'''Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.

What would be the base case(s) we’d have to consider for implementing this function?

How should our recursive solution converge on our base case(s)?'''

array = [5,6,7,8,4,5,9,3]

def recursive_search(array, target):
  # create a base case
  base = False
  if array[0] == target:
    base =  True
    print("Found it")
    return base
  if array[0] != target and len(array) > 1:
    print("looking")
    return recursive_search(array[1:], target)
  else:
    print("Number not found")
    

recursive_search(array, 1)