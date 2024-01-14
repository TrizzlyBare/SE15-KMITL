#No.1

import matplotlib.pyplot as plt

def pie_chart(data):
    grouped_data = {}
    for item in data:
        if item in grouped_data:
            grouped_data[item] += 1
        else:
            grouped_data[item] = 1

    values = grouped_data.values()

    plt.pie(values, startangle=140)
    plt.axis('equal')
    plt.show()

pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])

#====================================================================================================

#No.2

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([3,2,9,7,8]))

#====================================================================================================

#No.3

def my_union(a, b):
    result = a[:]
    for x in b:
        if x not in result:
            result.append(x)
    return result

def my_intersection(a, b):
    result = []
    for x in a:
        if x not in result and x in b:
            result.append(x)
    return result

def my_difference(a, b):
    result = []
    for x in a:
        if x not in b and x not in result:
            result.append(x)
    return result

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))

#====================================================================================================

#No.4

def print_table(table):
    max_lengths = [0] * len(table[0])

    for row in table:
        for i, item in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(item)))

    for row in table:
        for i, item in enumerate(row):
            print(str(item).ljust(max_lengths[i]), end=" ")
        print()

print_table([["X","Y"], [0,0], [10,10], [200,200]])

print_table( [
    ["ID","Name","Surname"], 
    ["001","Guido","van Rossum"], 
    ["002","Donald","Knuth"], 
    ["003","Gordon","Moore"] ] )

#====================================================================================================

#No.5

def isAnagram(String1, String2):
    if len(String1) != len(String2):
        return False
    for i in String1:
        if i not in String2:
            return False
    return True

print(isAnagram("silent", "listen"))
print(isAnagram("anagram", "nagaram"))

#====================================================================================================