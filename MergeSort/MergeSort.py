# MergeSort : Time Complexity O(n log(n)) / Space Complexity O(1)

# Divide : Split and recursively call the two parts
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    middleIdx = len(lst)//2
    left = lst[:middleIdx]
    right = lst[middleIdx:]
    # Recursive calls on each half
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    # Merge
    merge = mergeSortlist(left_sorted, right_sorted, lst)
    return merge


# Conquer : Merge two sorted list with no extra space : Space O(1)
def mergeSortlist(left, right, lst):
    # Iterator for the main list
    k = 0
    # Iterators traversing the two halves
    i = 0
    j = 0
    # Merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    # All remaining values
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
    return lst

