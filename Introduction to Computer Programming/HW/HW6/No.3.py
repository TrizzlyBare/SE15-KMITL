num = int(input("Enter a number between 0 and 999: "))

def number_to_words(n):
    r1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    r2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    r3 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if n == 0:
        return "zero"
    elif n >= 1 and n <= 9:
        return r1[n - 1]
    elif n >= 10 and n <= 19:
        return r3[n - 11]
    elif n >= 20 and n <= 99:
        tens_digit = n // 10
        ones_digit = n % 10
        if ones_digit == 0:
            return r2[tens_digit - 1]
        else:
            return r2[tens_digit - 1] + " " + r1[ones_digit - 1]
    elif n >= 100 and n <= 999:
        hundreds_digit = n // 100
        remaining_digits = n % 100
        if remaining_digits == 0:
            return r1[hundreds_digit - 1] + " hundred"
        else:
            return r1[hundreds_digit - 1] + " hundred and " + number_to_words(remaining_digits)
    else:
        return "Number out of range"

if num < 0 or num > 999:
    print("I don't know.")
else:
    words = number_to_words(num)
    print(words)
