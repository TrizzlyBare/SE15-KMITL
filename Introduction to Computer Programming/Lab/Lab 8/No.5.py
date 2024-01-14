def LCS(s1, s2):
    m = len(s1)
    n = len(s2)

    counter = [[0] * (n + 1) for x in range(m + 1)]
    longest = 0

    if m == 0 or n == 0:
        return ""

    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(s1[i - c + 1:i + 1])
                elif c == longest:
                    lcs_set.add(s1[i - c + 1:i + 1])

    return lcs_set.pop() if longest > 0 else ""

print(LCS("ingenious", "intelligent")) 
print(LCS("philosophically", "zoophilous"))  
print(LCS("intelligent", "inconsidered"))  
print(LCS("russian", "ukrainian"))  
print(LCS("war", "love"))
print(LCS("romanian", "rominiranian"))  
