# Selection Sort : Time Complexity O(n^2)  / Space Complexity O(1) Space
def selection_sort(data):
    for i in range(len(data) - 1):
        smallestIdx = i
        for j in range(i + 1, len(data), 1):
            if data[j] < data[smallestIdx]:
                smallestIdx = j
        if smallestIdx != i:
            data[smallestIdx], data[i] = data[i], data[smallestIdx]
    return data
