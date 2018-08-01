# Sorting Algorithm in Python

A sorting algorithm is an algorithm that puts elements of an array in a certain order.

### Features:
- In place: strictly an in-place sort algorithm needs only O(1) memory beyond the items being sorted.(no needs for extra memory)

- Recursive: some sorting algorithm are implemented in a recursive manner.(Dive and Conquer)

- Stable: stable sorting algorithms maintain the relative order of records with equal values.

### Lower Bound

For sorting N items we have to make Log(N!) comparaisons. With stringling formula it can be reduced to N log(N).
- N log(N) time complexity is the lower bound for comparaison based sorting algorithms.

- We can achieve O(N) running time as far as sorting is concerned with non comparaison based algorithms.(Bucket Sort or Radix Sort)
