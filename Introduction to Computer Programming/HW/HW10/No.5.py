def isAnagram(String1, String2):
    if len(String1) != len(String2):
        return False
    for i in String1:
        if i not in String2:
            return False
    return True

print(isAnagram("silent", "listen"))
print(isAnagram("anagram", "nagaram"))