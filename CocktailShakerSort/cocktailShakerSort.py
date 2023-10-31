# Cocktail Shaker Sort : Big O(n^2)

def cocktail_shaker(array):
    isSorted = False
    start = 0
    end = len(array) - 1
    while not isSorted:
        isSorted = True

        # Comparison from Left to Right
        for i in range(start, end):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False

        end -= 1

        # Comparison from Right to Left
        for j in reversed(range(start - 1, end - 1)):
            if array[j] > array[j + 1]:
                swap(j, j + 1, array)
                isSorted = False

        start += 1

    return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

# Test
a = [3, 4, 2, 0, 1]
print(cocktail_shaker(a))
