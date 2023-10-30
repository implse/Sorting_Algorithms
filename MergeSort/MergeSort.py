# MergeSort : Time Complexity O(n log(n)) / Space Complexity O(1)

# Divide : Split and recursively call the two parts
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)


# Conquer : Merge two sorted list with no extra space : Space O(1)
def merge(first, second):
  result = []
  i = 0
  j = 0
  while i < len(first) and j < len(second):
    if first[i] < second[j]:
      result.append(first[i])
      i += 1
    else:
      result.append(second[j])
      j += 1
  if len(first[i:]) > 0:
      result.extend(first[i:])
  if len(second[j:]) > 0:
      result.extend(second[j:])
  return result

