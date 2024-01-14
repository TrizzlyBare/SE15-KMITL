# se = set([1, 2, 3])
# se = set([1, 2, 3, 4])
# se = set([1, 2, 3, 4, 5])

def powers(s):
    if len(s) == 0:
        return {frozenset()}

    element = s.pop()
    subsets_without_element = powers(s)

    subsets_with_element = {subset.union({element}) for subset in subsets_without_element}

    return subsets_without_element.union(subsets_with_element)


def power2(x):
    if len(x) == 0:
        return {frozenset()}

    element = x.pop()
    subsets_without_element = power2(x)

    subsets_with_element = {subset.union({element}) for subset in subsets_without_element}

    return subsets_without_element.union(subsets_with_element)

s = {1, 2, 3, 4}
power_set = powers(s)
print(power_set)

x = frozenset([0, 1, 2])
print(x)