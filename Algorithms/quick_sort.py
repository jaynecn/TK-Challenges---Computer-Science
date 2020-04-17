# What will the contents of the array below be after each pass of the Quick Sort algorithm? (assume the first element is chosen as the pivot)

# 24 44 12 99 3 56
# step 1 choose pivot - 1st element on the left.
# 24 44 12 99 3 56 #sort next element, no swaps.
# 12 24 44 99 3 56 # step 3 12 goes to the left of the pivot.
# 12 24 44 99 3 56 # step 3 99 stays to the right
# 3 12 24 44 99 56 # step 4 3 goes to the left of the pivot.
# 3 12 24 44 99 56 # 44 is the new pivot, no swaps.
# 3 12 24 44 56 99 # 99 is the new pivot, swaps 56 to the left of the pivot.

test1 = [20, 17, 19, 3, 2, 5, 1, 3, 8, 4, 10]
test2 = [4, 1, 3, 2]

# choose a pivot
# move all elements less than the pivot to the left.
# move all elements greater than the pivot to the right.

# for example
# Pivot => 3
# LHS = [1, 2]

# Pivot => 1
# LHS = []
# RHS = [2, 3]


def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  lhs, pivot, rhs = partition(arr)
  
  return quick_sort(lhs) + [pivot] + quick_sort(rhs)
  
  
def partition(arr):
  pivot = arr[0]
  lhs = []
  rhs = []
  
  for number in arr[1:]:
    if number <= pivot:
      lhs.append(number)
    else:
      rhs.append(number)
      
  return lhs, pivot, rhs
  

print(quick_sort(test1))