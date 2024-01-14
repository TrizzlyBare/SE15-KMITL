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