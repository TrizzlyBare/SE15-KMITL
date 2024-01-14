num = int(input("Enter the number of lines: "))

for a in range(1, int(num / 2)+1):
    for b in range(a+1)[::-1]:
        print(2**b, end=" ")
    print()

for a in range(1, int(num/2) + 2)[::-1]:
    if num % 2 == 0 and a == (num/2)+1:
        continue
    for b in range(a+1)[::-1]:
        print(2**b, end=" ")
    print()