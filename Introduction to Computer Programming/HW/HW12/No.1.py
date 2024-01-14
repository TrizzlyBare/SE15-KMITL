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