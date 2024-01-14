def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([3,2,9,7,8]))

