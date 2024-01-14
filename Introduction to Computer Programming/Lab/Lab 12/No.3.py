def inverse(dict):
    new_dict = {}
    for key, value in dict.items():
        if value not in new_dict:
            new_dict[value] = set([key])
        else:
            new_dict[value].add(key)

    print(new_dict)

dict1 = {'a': '1', 'b': '2', 'c': '1', 'd': '3', 'e': '1', 'f': '2'}
inverse(dict1)
