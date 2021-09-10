# MergeSort : Time Complexity O(n log(n)) / Space Complexity O(1)
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    # Divide
    middleIdx = len(lst) // 2
    left = lst[:middleIdx]
    right = lst[middleIdx:]
    # Recursive calls on each half
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    # Merge
    merge_result = mergeSortlist(left_sorted, right_sorted, lst)
    return merge_result


# Helper : Merge two sorted list with no extra space : Space O(1)
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


# MergeSort : Time Complexity O(n log(n)) / Space Complexity O(n)
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    # Divide
    middleIdx = len(lst) // 2
    left = lst[:middleIdx]
    right = lst[middleIdx:]
    # Recursive calls on each half
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    # Merge
    merge_result = mergeSortlist(left_sorted, right_sorted)
    return merge_result

# Helper : Merge two sorted list with extra space for the sorted list : Space O(n)
def mergeSortlist(left, right):
    ln_left = len(left)
    ln_right = len(right)
    # Sorted list
    sortedlist = [None for _ in range(ln_left + ln_right)]
    # Iterators
    k = 0
    i = 0
    j = 0
    # Merge
    while i < ln_left and j < ln_right:
        if left[i] <= right[j]:
            sortedlist[k] = left[i]
            i += 1
        else:
            sortedlist[k] = right[j]
            j += 1
        k += 1
    # All remaining values
    while i < ln_left:
        sortedlist[k] = left[i]
        i += 1
        k += 1
    while j < ln_right:
        sortedlist[k] = right[j]
        j += 1
        k += 1
    return sortedlist

