 # Time O(n + k)
def counting_sort(array):
    # Find max value (k)
    maximum = max(array)
    being_sorted = [0 for _ in range(len(array))]
    frequency = [0 for _ in range(maximum + 1)]

    # Counts the number of occurrences of each digit in the input array
    for i in range(len(array)):
        index = array[i]
        frequency[index] += 1

    # Accumulate the frequency list
    for i in range(1, len(frequency)):
        frequency[i] = frequency[i] + frequency[i - 1]

    # Place input values in the correct position in sorted list
    for i in reversed(range(len(array))):
        index = frequency[array[i]] - 1
        being_sorted[index] = array[i]
        frequency[array[i]] -= 1

    return being_sorted


a = [9, 3, 1, 4, 5, 7, 7, 2, 2]
b = [9, 4, 1, 7, 9, 1, 2, 0]
print(counting_sort(a))
print(counting_sort(b))
