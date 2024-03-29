# Sorting Algorithms in Python

A sorting algorithm puts `items` of a `list` in a certain order.

Adavantages of sorting a list: 

  - Searching for an `item` in a `list` works much faster if the list is sorted. `Binary search` finds the position of a target `item` within a sorted list in `O(log n)`.

  - Searching for an `item` in a `list` based on their relationship to the rest of the `items` is easier when the list is `sorted`.

  -  Finding duplicate `item` in a `list` can be done very quickly when the `list` is sorted.

## Sorting Algorithms Classifications
Sorting algorithms can generally be classified into three distinct categories:

  - Comparison sorts (Bubble Sort, Quick Sort, Selection Sort)
  - Non-comparison sorts (Radix Sort, Counting Sort)
  - Others (Bogosort)

### Features:
- `In-place sorting`: an `in-place` sorting algorithm needs only `O(1)` memory. (no needs for extra memory)

- `Recursive sorting`: some sorting algorithms are implemented in a `recursive` manner. (Divide and Conquer)

- `Stable sorting`: stable sorting algorithms maintain the relative order of `items` with equal values.

Some examples of in-place sorting algorithms:

- Selection sort
- Insertion sort
- Bubble sort
- Heap sort

Some examples of recursive sorting algorithms:

- Merge sort
- Quicksort
- Heapsort
- Timsort

Some examples of stable  sorting algorithms:

- Insertion sort
- Merge sort
- Bubble sort
- Counting sort
- Radix sort
- Timsort


### Lower Bound

For sorting `n` items we have to make `Log(n!)` comparisons (the number of comparisons grows very quickly as the number of items increases). With Stirling's formula (Stirling's approximation) it can be reduced to `n log(n)`. This means that the worst-case number of comparisons required to sort n items is approximately n log(n).


- The `n log(n)` time complexity is the `lower bound` for comparison based sorting algorithms.

- We can achieve `O(n)` running time with non comparison based algorithms.(`Bucket Sort` or `Radix Sort`)

## Bubble Sort

Repeatedly steps through the list, compare each pair of adjacent `items` and `swaps` them if they are in the wrong order.

`Time Complexity : O(n^2)`

`Bubble Sort` has worst-case and average complexity in `O(n^2)`. It is not a efficient sorting algorithm.

`Bubble Sort`is an `in-place` algorithm.

## Insertion Sort


Insertion sort is a simple sorting algorithm that works by repeatedly inserting an element into the sorted portion of the array at the correct position.

It iterates over the list, finds the correct position forevery element, and inserts it there.

`Time Complexity : O(n^2)`

`Space complexity: O(1)`

`Insertion Sort`is an `in-place` algorithm.

## Merge Sort

`Merge Sort` is a divide and conquer algorithm that was invented by John Von Neumann in 1945.

- Comparison algorithm and stable sorting.

- Not `in-place` algorithm.

- `Merge Sort` is often the best choice for sorting a linked list.

`Time Complexity : O(n log(n))`

1 - Divide the array into two sub arrays recursively.

2 - Sort these sub-arrays recursively with `Merge Sort` again.

3 - If there is only a single item left in the sub-array, we consider it to be sorted by definition.

4 - Merge the sub-array to get the final sorted array.

- `Merge Sort` is often implement `recursively`.

## Quick Sort

`Quick sort` is the fastest, comparison based sorting algorithm for lists in the average case. When implemented well, it can be about two or three times faster than its main competitors, `Merge Sort` and `Heap Sort`.

- It is a divide and conquer algorithm.

- Often implement recursively.

-  It is still a commonly used algorithm for sorting.



It was developed by Tony Hoare in 1959.

`Time Complexity : O(n log(n))`

Not Stable. Does not keep the relative order of items with equal value.

In place, does not need any additional memory.

`Quick Sort` gained widespread adoption, appearing, for example, in Unix as the default library sort subroutine. Its name come from the C standard library subroutine `qsort`.

## Selection sort

The algorithm divides the input list into two parts:
  - The `sub-list` of `items` already sorted.
  - The `sub-list` of `items` remaining to be sorted that occupy the rest of the list.

The algorithm proceeds by finding the `smallest element` in the unsorted `sub-list` and puts it at the beginning of news sorted `sub-list`.

Selection Sort is iterative and goes through an unsorted `sub-list` transforming into a sorted list.

It is an in-place algorithm. (no need for extra memory)

Does not preserve the order of keys with equal values. (Not a stable sort)

`Time Complexity : O(n^2)`

`Space Complexity : O(1)`

## Radix Sort

`Radix Sort` is an integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value)

- Radix Sort has two variants :
  - MSD : Most Significant Digit
  - LSD : Least Significant Digit
- Numbers are bucketed based on the value of digits moving left to right for MSD or
right to left from LSD.
- Radix Sort is a non-comparison sort.

#### Most Significant Digit - MSD

`Radix Sort` works by processing an integer or integer representation starting from the greatest digit, and moving towards the least significant digit. This method is usually solved by recursion.

#### Least Significant Digit - LSD

`Radix` Sort works by processing the least significant (smallest) digit first, and moving towards the greater, move significant digit as it continue to sort. This method is usually solved iteratively, using counting sort or bucket sort internally.


`Time Complexity : O(n)`

Pseudo Code :
  - Takes numbers in an input list.
  - Passes through each digit in those numbers, from least to most significant.
  - Looks at the values of those digits.
  - Buckets the input list according to those digits.
  - Renders the results from that bucketing.
  - Repeats this process until the list is sorted.

## Counting Sort

`Counting Sort` is an efficient algorithm for sorting an array of positive integer. It is an integer sorting algorithm.

The ability to perform integer arithmetic on the keys allows integer sorting algorithms to be faster than comparison sorting algorithms in many cases.

Counting sort is an integer sorting algorithm. Values must be integers or integers string representation.

Counting sort is not a comparison based sorting algorithm, so linearithmic running time can be reduced.


It operates by counting the number of occurrences of each digit in the input array.

`Time Complexity : O(n + k)`

`n` : number of items we want to sort.
`k` : difference between the maximum and minimum values.

Only suitable if the variation in keys is not significantly greater than the number of items.


## Cocktail Shaker Sort

`Cocktail Shaker Sort` also known as bidirectional bubble sort is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. The algorithm differs from a `Bubble Sort` in that it sorts in both directions on each pass through the list.

`Time Complexity : O(n^2)`


## Tim Sort

`Tim Sort` is a sorting algorithm based on `Insertion Sort` and `Merge Sort` along with some internal logic to optimze the manipulation of large scale data.

`Tim Sort` is a very fast `O(n log(n))` stable sorting algorithm. It is one of the best sorting algorithm in terms of complexity and stability.

`Tim Sort` is an hybrid algorithm, an efficient combination of a number of other algorithms.

The algorithm finds subsequences of the data that are already ordered (runs) and uses them to sort the remainder more efficiently.

- A particular algorithm is used to split the input array into sub-arrays.
- Each sub-array is sorted with a simple `Insertion Sort`.
- The sorted sub-array are merge into one array with the use of `Merge Sort`.
