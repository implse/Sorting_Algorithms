# MergeSort - O(N log(N))

def merge_sort(data):
    if len(data) == 1:
        return
    middle_index = len(data) // 2
    left_half = data[:middle_index]
    right_half = data[middle_index:]

    # Divide Part Recursive
    merge_sort(left_half)
    merge_sort(right_half)

    # Conquer Part
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[k] = left_half[i]
            i = i + 1
        else:
            data[k] = right_half[j]
            j = j + 1
        k = k + 1
    while i < len(left_half):
        data[k] = left_half[i]
        k = k + 1
        i = i + 1
    while j < len(right_half):
        data[k] = right_half[j]
        k = k + 1
        j = j + 1

# Test

m = [6, 1, 5, 10, 3, 9, 2, 4, 8, 7]
merge_sort(m)
print(m)
