original = [4, 3, 2, 6, 5, 1]

def bubbleSort(array):
    for arr in range(len(array) - 1):
        if array[arr] > array[arr+1]:
            array[arr], array[arr+1] = array[arr+1], array[arr]
            bubbleSort(array)
        print(array)

print(bubbleSort(original))
