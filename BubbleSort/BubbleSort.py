# Bubble Sort - O(n^2)

def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Test

# d = [1, 5, 3, 2, 4, 8, 7]
# print(bubble_sort(d))
