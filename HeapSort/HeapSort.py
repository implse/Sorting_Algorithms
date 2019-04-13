# Heap Sort Time O(n log n) / Space O(1)
def heap_Sort(array):
    # Build Max Heap from input
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        sifDown(0, endIdx - 1, array)
    return array

def swap(i, j,  array):
    array[i], array[j] = array[j], array[i]

def buildMaxHeap(array):
    firstParentIdx = (len(array) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        sifDown(currentIdx, len(array) - 1, array)

def sifDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else - 1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return
