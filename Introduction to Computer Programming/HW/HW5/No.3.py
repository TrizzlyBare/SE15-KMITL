n = int(input("Enter the number greater or equal to 1 : "))

if n >= 1 :
    for f in reversed(range(n)):
        for i in range(f + 1):
            for j in range(i +1):
                print("*", end = "")
            print("")
        for i in reversed(range(f + 1)):
            for j in range(i):
                print("*", end = "")
            if i == 1 :
                continue
            else:
                print("")
else :
    ("Invalid Input")

