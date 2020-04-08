# What will the contents of the array below be after each pass of the Quick Sort algorithm? (assume the first element is chosen as the pivot)

24 44 12 99 3 56
# step 1 choose pivot - 1st element on the left.
24 44 12 99 3 56 #sort next element, no swaps.
12 24 44 99 3 56 # step 3 12 goes to the left of the pivot.
12 24 44 99 3 56 # step 3 99 stays to the right
3 12 24 44 99 56 # step 4 3 goes to the left of the pivot.
3 12 24 44 99 56 # 44 is the new pivot, no swaps.
3 12 24 44 56 99 # 99 is the new pivot, swaps 56 to the left of the pivot.