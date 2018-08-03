# Quick Sort

def quick_sort(data, low, high):
    if low >= high:
        return
    pivot_index = partition(data, low, high)
    quick_sort(data, low, pivot_index - 1)
    quick_sort(data, pivot_index + 1, high)

def partition(data, low, high):

    pivot_index = (low + high) // 2
    swap(data, pivot_index, high)

    i = low

    for j in range(low, high, 1):
        if data[j] <= data[high]:
            swap(data, i, j)
            i = i + 1
    swap(data, i, high)

    return i

def swap(data, i, j):
    data[i], data[j] = data[j], data[i]
