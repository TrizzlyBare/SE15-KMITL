def get_the_difference(list1, list2):
    new_list = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            new_list.append(list1[i])
    for i in range(len(list2)):
        if list2[i] not in list1:
            new_list.append(list2[i])
    return new_list

print(get_the_difference([3,1,1,1,2,7],[4,1,1,2,2,5]))
