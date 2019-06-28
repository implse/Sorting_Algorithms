# MergeSort : Time Complexity O(n log(n))
def mergeSort(array):
    if len(array) == 1:
        return array
    # Divide
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    # Recursive Calls
    left_sorted = mergeSort(leftHalf)
    right_sorted = mergeSort(rightHalf)
    # Merge
    merge_result = mergeSortArray(left_sorted, right_sorted)
    return merge_result

def mergeSortArray(leftHalf, rightHalf):
    ln_leftHalf = len(leftHalf)
    ln_rightHalf = len(rightHalf)
    sortedArray = [None for _ in range(ln_leftHalf + ln_rightHalf)]
    k = i = j = 0
    while i < ln_leftHalf and j < ln_rightHalf:
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < ln_leftHalf:
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < ln_rightHalf:
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray
