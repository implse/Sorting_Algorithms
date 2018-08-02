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

## Bubble Sort

Repeatedly steps through the list to be sorted, compare each pair of adjacent items and swaps them if they are in the wrong order.

Time Complexity : O(N^2)

Bubble Sort has worst-case and average complexity both O(N^2). It it not a practical sorting algorithm.

In-place algorithm.

## Merge Sort

Merge Sort is a divide and conquer algorithm that was invented by John Von Neumann in 1945.

- Comparaison algorithm and stable sorting.

- Not in place algorithm.

- Merge sort is often the best choice for sorting a linked list.

Time Complexity : N log(N)

1 - Divide the array into two sub arrays recursively.

2 - Sort these sub arrays recursively with Merge Sort again.

3 - If there is only a single item left in the sub array, we consider it to be sorted by definition.

4 - Merge the sub array to get the final sorted array.

- Often implement recursively.
