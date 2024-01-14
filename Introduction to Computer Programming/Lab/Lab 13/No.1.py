#define a recursive function to check a membership in a list

def list_member(value, list):
    if len(list) == 0:
        return False
    elif value == list[0]:
        return True
    else:
        return list_member(value, list[1:])
    
print(list_member(2, [1,2,3]))
