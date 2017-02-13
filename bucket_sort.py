original = [5, 1, 0, 5, 0, 9, 0, 0, 0, 3, 0, 7]

def bucket_sort(a):
  if len(a) < 1:
    return a

  # search for the largest value
  # "max" is a reserved keyword in python.
  maxx = a[0]
  for item in a:
    maxx = max(maxx, item)

  # create a list of all zeroes the size of maxx
  tally = [0] * (maxx + 1)

  # Go through the original array and increment the tally for
  # each number. The tallies are kept at the array index of the
  # value itself. Zeros are counted at index 0, ones are counted at index 1.
  for i, item in enumerate(a):
    tally[item] += 1

  # create a new array that will be the final sorted array
  sorted_a = []

  # iterate through each of the tallies for each value.
  for i, count in enumerate(tally):
    if count > 0:
      # Append the number to the sorted array the number of times that
      # it was tallied.
      # (use an underscore to indicate we're not using the value of i
      # we're just doing something i times.)
      for _ in range(count):
        sorted_a.append(i)
  return sorted_a

def insertion_sort(a):
  # go over each spot in the array from beginning to end
  for i in range(len(a)):
    index = i
    min_value = a[i]
    # search the remaining array for the smallest value
    for n in range(i + 1, len(a)):
      if a[n] < min_value:
        min_value = a[n]
        index = n
    # swap the minimum value with the value at the location we're searching from.
    a[i], a[index] = min_value, a[i]
  return a

print(bucketSort(original))
