isbn_num = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if len(isbn_num) != 9:
    print("Invalid input.")
    exit()

check = 0
for i in range(len(isbn_num)):
    check += int(isbn_num[i]) * (i + 1)
    check %= 11

if check == 10:
    print(f"The ISBN-10 number is {isbn_num}X")

else:
    print(f"The ISBN-10 number is {isbn_num}{check}")
