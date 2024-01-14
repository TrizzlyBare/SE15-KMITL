def merge(list1, list2):
    merged_list = []
    i, j = 0, 0

    for _ in range(len(list1) + len(list2)):
        if i < len(list1) and (j >= len(list2) or list1[i] < list2[j]):
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    print(f"The merged list is {merged_list}")
    return merged_list

first_list = [1, 3, 5, 7, 9]
second_list = [2, 4, 6, 8 ,10]
merged_list = merge(first_list, second_list)

first_list1 = [1, 1, 1, 1, 8, 8, 8, 8, 8, 15, 15, 15, 15]
second_list2 = [2, 4, 6, 8, 10]
merged_list = merge(first_list1, second_list2)
