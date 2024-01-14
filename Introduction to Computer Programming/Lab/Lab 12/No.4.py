#Given two sets, sub and sup, write a Python function is_subset(sub, sup) that returns True if sub is a subset of sup, otherwise returns False. You must not sub.issubset(sup) or sub <= sup

# sup = set([1, 2, 3, 4])
# sub = set([1, 2, 4])

sup = set([1, 2, 3, 4])
sub = set([1, 2, 5])

def is_subset(sub, sup):
    for i in sub:
        if i not in sup:
            return False
    return True

print(is_subset(sub, sup))