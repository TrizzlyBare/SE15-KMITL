def product(*sets):
    if len(sets) == 1:
        return sets[0]
    else:
        result = set()
        for x in sets[0]:
            for y in product(*sets[1:]):
                result.add((x,y))
        return result

s1 = set([1,2,3])
s2 = set(['p','q'])
s3 = set(['a','b','c'])

print(product(s1,s2))
print(product(s1, s2, s3))
print(product(s1))