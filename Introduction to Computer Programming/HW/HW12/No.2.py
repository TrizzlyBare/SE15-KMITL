def composite(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if dict1[key] in dict2:
            dict3[key] = dict2[dict1[key]]
    return dict3

dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

print(composite(dict1, dict2))