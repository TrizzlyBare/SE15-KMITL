number = input("Enter the number : ")

if number.isnumeric() == False:
    print("Input invalid")

elif number.isdigit():
    userIn = int(input("Bi(1),Oct(2),Hex(3),Dec(4) : "))
    if userIn == 1:
        print(format(int(number), "e"))
    elif userIn == 2:
        print(format(int(number), "o"))
    elif userIn == 3:
        print(format(int(number), "x"))
    elif userIn == 4:
        print(format(int(number), "d"))
    else:
        print("Incorrect input")


elif number.replace(".", "").isnumeric() or float(number) < 0:
    userIn = int(input("Display floating point(1), Scientific format(2) : "))
    if userIn == 1:
        print(format(float(number), ".2f"))
    elif userIn == 2:
        print(format(float(number), ".2e"))
    else:
        print("Incorrect input")