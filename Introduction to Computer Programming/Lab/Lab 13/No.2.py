#Define a recursive function to reverse a list

def list_reverse(list):
    if len(list) == 0:
        return []
    else:
        return list_reverse(list[1:]) + [list[0]]
    
print(list_reverse([1,2,3]))