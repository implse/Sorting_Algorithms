def counting_sort(to_be_sorted, digit, radix):
    # Create a list being_sorted which will be the sorted list
    being_sorted = [0]*len(to_be_sorted)
    count = [0]*int(radix)
    
    # Counts the number of occurences of each digit in to_be_sorted
    # count[i] is the value of the number of elements in to_be_sorted equal to i
    for i in range(0, len(to_be_sorted)):
        digit_of_Ai = int((to_be_sorted[i]/radix**digit)%radix)
        count[digit_of_Ai] = count[digit_of_Ai] + 1

    # Change count to show the cumulative # of digits up to that index of count
    # count is modifed to have the number of elements <= i
    for j in range(1, radix):
        count[j] = count[j] + count[j-1]

    # go through to_be_sorted backwards)
    for m in range(len(to_be_sorted) -1, -1, -1):
        digit_of_Ai = int((to_be_sorted[m]/radix**digit)%radix)
        count[digit_of_Ai] = count[digit_of_Ai] -1
        being_sorted[count[digit_of_Ai]] = to_be_sorted[m]

    return being_sorted

a = [9,3,1,4,5,7,7,2,2]
print(counting_sort(a, 0, 10))
