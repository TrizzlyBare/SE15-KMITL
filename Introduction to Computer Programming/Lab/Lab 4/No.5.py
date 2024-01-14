s = 0

for i in range(5):
    num = int(input("Enter an interger: "))
    if (s >= 0 and num >= 0) or (s < 0 and num < 0):
        s += num
    else:
        s = num
    
    print(f"current sum: {s}")