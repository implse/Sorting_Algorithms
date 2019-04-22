# Quick Sort : Time Complexity O(n log(n)) / Space Complexity O(log(n))
def quickSort(array):
	quicksortHelper(array, 0, len(array) - 1)
	return array

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

def partition(array, low, high):
	pivotIdx = (low + high) // 2
	swap(array, pivotIdx, high)
	i = low
	for j in range(low, high, 1):
		if array[j] <= array[high]:
			swap(array, i, j)
			i += 1
	swap(array, i, high)
	return i

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
