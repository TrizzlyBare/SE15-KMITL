while True:
    i = int(input("Enter an integer: "))

    if i == 0:
        print("It is 0.")
        break

    elif i < 0:
        print("It is negative.")
        break

    else:
        binary_str = ""
        while i > 0:
            binary_str = str(i % 2) + binary_str
            i //= 2
        print(f"{binary_str[::-1]}")

    decimal = 0
    power = 0

    for i in binary_str[::-1]:
        decimal += int(i) * (2 ** power)
        power += 1

    print(f"{decimal} is the decimal representation of {binary_str[::-1]}.")
