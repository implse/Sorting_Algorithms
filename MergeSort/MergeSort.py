# MergeSort : Time Complexity O(n log(n))
def merge_sort(data):
    # Base Case
    if len(data) == 1:
        return
    middle_index = len(data) // 2
    # Divide
    left_half = data[:middle_index]
    right_half = data[middle_index:]
    # Recursive Divide
    merge_sort(left_half)
    merge_sort(right_half)
    # Merge
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[k] = left_half[i]
            i +=  1
        else:
            data[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        data[k] = left_half[i]
        k += 1
        i += 1
    while j < len(right_half):
        data[k] = right_half[j]
        k += 1
        j += 1
