def perm2(t, current=[]):
    if len(current) == 2:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm2(t[:i] + t[i+1:], current + [t[i]])

t = [1, 2, 3]
perm2(t)

def perm3(t, current=[]):
    if len(current) == 3:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm3(t[:i] + t[i+1:], current + [t[i]])

t = [1, 2, 3, 4]
perm3(t)

def perm(t, n, current=[]):
    if len(current) == n:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm(t[:i] + t[i+1:], n, current + [t[i]])

perm((1,2,3,4), 4)