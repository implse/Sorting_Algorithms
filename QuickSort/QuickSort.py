 # Quick Sort : Time Complexity O(n log(n)) / Space Complexity O(log(n))

# Main Function
def quickSort(array):
	quicksortHelper(array, 0, len(array) - 1)
	return array

# Recursive Function
def quicksortHelper(array, low, high):
	# Base case
	if low >= high:
		return
	# Pivot
	pivotIdx = partition(array, low, high)
	# Recursive call left
	quicksortHelper(array, low, pivotIdx - 1)
	# Recursive call right
	quicksortHelper(array, pivotIdx + 1, high)

# Partition Function : partition the array around the pivot
def partition(array, low, high):
	# Choosing a pivot in the middle
	pivotIdx = (low + high) // 2
	# Swap pivot with last value in the array
	swap(array, pivotIdx, high)
	i = low
	for j in range(low, high):
		if array[j] <= array[high]:
			swap(array, i, j)
			i += 1
	# Moving the pivot at the right place
	swap(array, i, high)
	# Return the pivot index
	return i

# Swap Function
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
