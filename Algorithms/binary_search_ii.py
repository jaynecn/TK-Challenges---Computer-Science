arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def binary_search(arr, target):
  
# find middle of array, that is the starting point
  low = 0
  high = len(arr) - 1
  found = False
  print(type(target))
  while low <= high and not found:
    middle = int((low + high)/2)
    
    if (type(target) != int):
      print (f"target is not recognised, try again")
      found = True
    elif (arr[middle] == target):
      print (f"Here is the location of the target({target}): array position {arr[middle]}")
      found = True
    elif (target < arr[middle]):
      high = middle - 1
    elif (target > arr[middle]):
      low = middle + 1
    else:
      print (f"Not recognised")
  return found


   
binary_search(arr, 5) 
