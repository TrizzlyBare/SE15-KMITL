def find_duplicates(dict):
    new_dict = {}
    for key in dict:
        for key2 in dict:
            if key != key2 and dict[key] == dict[key2]:
                new_dict[key] = dict[key]
    print(new_dict)

myDict = {'s5301':'Fred', 's5302':'Harry', 's5303':'John', 's5304':'Fred', 's5305':'Harry'}
find_duplicates(myDict)