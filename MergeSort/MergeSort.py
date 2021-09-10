# MergeSort : Time Complexity O(n log(n))
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    # Divide
    middleIdx = len(lst) // 2
    leftHalf = lst[:middleIdx]
    rightHalf = lst[middleIdx:]
    # Recursive calls on each half
    left_sorted = mergeSort(leftHalf)
    right_sorted = mergeSort(rightHalf)
    # Merge
    merge_result = mergeSortlist(left_sorted, right_sorted)
    return merge_result

# Helper : Merge two sorted list
def mergeSortlist(leftHalf, rightHalf):
    ln_leftHalf = len(leftHalf)
    ln_rightHalf = len(rightHalf)
    # Sorted list
    sortedlist = [None for _ in range(ln_leftHalf + ln_rightHalf)]
    # Iterators
    k = i = j = 0
    # Merge
    while i < ln_leftHalf and j < ln_rightHalf:
        if leftHalf[i] <= rightHalf[j]:
            sortedlist[k] = leftHalf[i]
            i += 1
        else:
            sortedlist[k] = rightHalf[j]
            j += 1
        k += 1
    # All remaining values
    while i < ln_leftHalf:
        sortedlist[k] = leftHalf[i]
        i += 1
        k += 1
    while j < ln_rightHalf:
        sortedlist[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedlist
