while True:
    character = input("Enter a character (Press Tab to exit): ")

    if character == '\t':
        print("Program terminated.")
        break

    if len(character) == 1:
        ascii_code = ord(character)

        if 65 <= ascii_code <= 90:
            lowercase_letter = chr(ascii_code + 32)
            print(f"{character} is a capital letter and its small-case letter is {lowercase_letter}")

        elif 97 <= ascii_code <= 122:
            uppercase_letter = chr(ascii_code - 32)
            print(f"{character} is a small-case letter and its capital letter is {uppercase_letter}")

        elif 48 <= ascii_code <= 57:
            print(f"{character} is a numeric character")

        else:
            print(f"{character} is a special character")
