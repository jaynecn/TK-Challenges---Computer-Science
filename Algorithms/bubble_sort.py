test = [22, 17,19, 2, 5, 1, 3, 8, 4, 10]

test2 = [4, 3, 2, 1]
#compare element with the element immediately after it
# 1st iteration [3,2,1,4]
# 2nd iteration [2,1,3,4]
# 3rd iteration [1,2,3,4]

def bubble_sort(arr):
  # length of list
  length = len(arr)
  
  if length <= 1:
    return arr
  
  for i in range(length):
    didSwap = False
    
    for j in range(length - 1):
    # for j in range(length - i - 1): MORE EFFICIENT
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        didSwap = True
        
    if didSwap is False:
      break
    
  
  return arr


print(bubble_sort(test))

def bubble_sort_2(arr):
    # loop through the whole array
    for index in range(len(arr)):
        # compare the number next to the first (index + 1) until you loop through the whole array
        for compared_num in range(index + 1, len(arr)):
            # if lhs > rhs
            if arr[index] > arr[compared_num]:
                print(f"{arr[index]} is greater than {arr[compared_num]}")
                # swap
                arr[index], arr[compared_num] = arr[compared_num], arr[index]
                # print(arr)
    # return array
    return arr
print("\nBubble sort")
print('[1, 5, 8, 3, 7]')
print(bubble_sort_2([1, 5, 8, 3, 7]))