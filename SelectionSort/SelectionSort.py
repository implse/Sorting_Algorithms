# Selection Sort : Time Complexity O(n^2)  / Space Complexity O(1) Space
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        if min_idx != i:
            data[min_idx], data[i] = data[i], data[min_idx]
    return
