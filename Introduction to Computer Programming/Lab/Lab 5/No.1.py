num = int(input("Enter the number : "))

for x in range(num):
    for y in range(x+1):
        print(y+1, end="") 
    print()

for x in reversed(range(num)):
    for y in range(x+1):
        print(y+1, end="") 
    print()