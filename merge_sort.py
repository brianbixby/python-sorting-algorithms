original = [5, 1, 0, 5, 0, 9, 0, 0, 0, 3, 0, 7]

def merge_sort(a):
  # single or zero-element arrays are always sorted!
  if len(a) < 2:
    return a

  # split a into two halves
  # force integer division.
  left = a[:len(a) // 2]
  right = a[len(a) // 2:]
  print('left:', left)
  print("right: ", right)

  # recursively merge_sort those two halves
  a1 = merge_sort(left)
  a2 = merge_sort(right)

  # merge the two halves together by traversing each array in
  # order simultaneously and always taking the smaller of the two.
  sorted_a = []
  i1 = 0
  i2 = 0
  for _ in range(len(a1) + len(a2)):
    if not i1 < len(a1):
      sorted_a.append(a2[i2])
      i2 += 1
    elif not i2 < len(a2):
      sorted_a.append(a1[i1])
      i1 += 1
    elif a1[i1] < a2[i2]:
      sorted_a.append(a1[i1])
      i1 += 1
    else:
      sorted_a.append(a2[i2])
      i2 += 1
  return sorted_a


print(merge_sort(original))
