# What will the contents of the array below be after each pass of the Merge Sort algorithm?

39 51 7 14 3 86
# step 1 - turn into individual sub-sets
39 51 7 14 3 86 # step 2 join into sub-sets of two numbers.  Check the first set.  They are in order (no swaps)
39 51 7 14 3 86 # step 3 middle sub-set is in order, no swaps.
39 51 7 14 3 86 # step 4 last sub-set is in order, no swaps.
7 39 51 14 3 86 # step 5 join into sub-arrays of three numbers.  Sort first-subarry into order.
7 39 51 3 14 86 # step 6 sort second sub-array.
3 7 14 39 51 86 # step 7 join into a sub-set of 6 numbers.  Sort the sub-array into order.