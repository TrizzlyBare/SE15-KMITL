#No.1

abbreviation = {"be": "b", "because": "cuz", "see": "c", "the": "da", "okay": "ok", "are": "r", "you": "u",
                "without": "w/o", "why": "y", "see you": "cu", "ate": "8", "great": "gr8", "mate": "m8",
                "wait": "w8", "later": "l8r", "tomorrow": "2mro", "for": "4", "before": "b4", "once": "1ce",
                "and": "&", "Your": "ur", "You're": "ur", "As far as I know": "afaik", "As soon as possible": "ASAP",
                "At the moment": "atm", "Be right back": "brb", "By the way": "btw", "For your Information": "FYI",
                "In my humble opinion": "imho", "In my opinion": "imo", "Laughing out loud": "lol", "Oh my god": "omg",
                "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

def textese(s):
    for key in abbreviation:
        s = s.replace(key, abbreviation[key])
    return s

def untextese(s):
    words = s.split()
    newText = []

    for word in words:
        found_abbreviation = False

        for key, value in abbreviation.items():
            if value == word:
                word = key
                found_abbreviation = True
            elif value in word:
                word = word.replace(value, key)
                found_abbreviation = True

        newText.append(word if not found_abbreviation else word)

    return ' '.join(newText)

print(textese("see you tomorrow"))
print(textese("As far as I know, you're great!"))

print(untextese("cu 2mro"))
print(untextese("imo ur gr8!"))

#No.2

def composite(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if dict1[key] in dict2:
            dict3[key] = dict2[dict1[key]]
    return dict3

dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

print(composite(dict1, dict2))

#No.3

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