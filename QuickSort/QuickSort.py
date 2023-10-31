 # Quick Sort : Time Complexity O(n log(n)) / Space Complexity O(1)

def quick_sort(nums, low, high):
	if low < high:
		split_idx = partition(nums, low, high)
		quick_sort(nums, low, split_idx - 1)
		quick_sort(nums, split_idx, high)
	return None

# Partition Function O(n): partition the list and swap values
def partition(nums, low, high):
	pivot = nums[high]
	i = low
	for j in range(low, high):
		if nums[j] < pivot:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
	nums[i], nums[high] = nums[high], nums[i]
	return i
