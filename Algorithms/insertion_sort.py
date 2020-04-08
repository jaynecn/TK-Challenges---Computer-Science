# What will the contents of the same array look like after each pass of the Insertion Sort algorithm?

25 67 4 33 19 40

25 67 4 33 19 40 # step 1 (no swaps)
4 25 67 33 19 40 # step 2
4 25 33 67 19 40 # step 3
4 19 25 33 67 40 # step 4
4 19 25 33 40 67 # step 5

"""
- **Insertion Sort** is an _in-place_ algorithm, meaning that it 
  does not require any additional memory to perform the sort operation.

- It works by conceptually dividing the array into _sorted_ and _unsorted_ pieces.

    1. Consider element at index 0 to be our  _sorted_ piece. The rest of the array is our _unsorted_ piece.

    2. Save the 1st element in the _unsorted_ piece in a temp variable.

    3. Shift elements in the _sorted_ piece over to the right until we find where the element 
       from step 2 should go.

    4. Insert the element from step 2 into its correct index within the _sorted_ piece.

    5. Repeat steps 2-4 until all elements have been processed.
"""

def in_sort2(list):
  # loop over n - 1 elements
  for i in range(1, len(list)):
    # save initial element to temp variable
    temp = list[i]
    # set inner loop index to current index
    j = i
    # inner loop
    while j > 0 and temp < list[j - 1]:
      # shift left until correct position found
      list[j] = list[j - 1]
      # decrement inner index
      j -=1
    # insert temp at correct position
    list[j] = temp
  # return our list
  return list

my_nums = [23, 34, 60, 1, 4, 5, 2]
my_names = ['Dave', 'Steve', 'Bob']

print(my_nums)
in_sort2(my_nums)
print(my_nums)

print(my_names)
in_sort2(my_names)
print(my_names)