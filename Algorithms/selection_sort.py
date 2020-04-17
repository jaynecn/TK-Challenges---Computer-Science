# # What will the contents of the array below look like after each pass of the Selection Sort algorithm?

# 25 67 4 33 19 40

# 4 67 25 33 19 40 # step 1
# 4 19 25 33 67 40 # step 2
# 4 19 25 33 67 40 # step 3 (no swaps)
# 4 19 25 33 67 40 # step 4 (no swaps)
# 4 19 25 33 40 67 # step 5

# for every index in the collection from 0 to length-2:
#compare the element at the current index, i, with everything on the right to identify the position of the smallest element
# swap the element at i with the smallest element
# i++

# insertion sort starts at left side, selection sort starts at the right - by finding the smallest element in the whole array first and putting it at index[0]

my_nums = [23, 34, 60, 1, 4, 5, 2]

def selection_sort(arr):
  #loop through n - 1 elements
  # looping through whole array
  for i in range(0, len(arr) - 1):
    # hold current
    current = i
    # hold smallest number index
    smallest = current
    
    # find next smallest element
    for j in range(current + 1, len(arr)):
      # save smallest element
      if arr[j] < arr[smallest]:
        smallest = j
      
    # current different than smallest?
    if current != smallest:
      # swap both values
      arr[current], arr[smallest] = arr[smallest], arr[current]
    
  return arr
      
print(my_nums)
selection_sort(my_nums)
print(my_nums)