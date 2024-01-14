character = input("Enter a character: ")

if len(character) == 1:
    ascii_code = ord(character)

    if 65 <= ascii_code <= 90:  
        lowercase_letter = chr(ascii_code + 32)
        print(f"{character} is a capital letter and its capital letter is {lowercase_letter}")

    elif 97 <= ascii_code <= 122:  
        uppercase_letter = chr(ascii_code - 32)
        print(f"{character} is a small-case letter and its capital letter is {uppercase_letter}")

    elif 48 <= ascii_code <= 57:  
        print(f"{character} is a numeric character")

    else:
        print(f"{character} is a special character")
else:
    print("Please enter a single character.")