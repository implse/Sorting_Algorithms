def selection_sort(data):
    for i in range(len(data) - 1):
        index = i
        for j in range(i + 1, len(data), 1):
            if data[j] < data[index]:
                index = j
        if index != i:
            data[index], data[i] = data[i], data[index]
    return data
