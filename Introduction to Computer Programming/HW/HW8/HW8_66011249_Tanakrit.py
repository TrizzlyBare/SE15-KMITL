#No.1

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

#=======================================================================================================================

#No.2

string = input("Enter some text: ")
count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

length = len(string)

print("-- Character Frequency Table --")
print("char percentage (character count / string length)")
for char, char_count in count.items():
    percentage = (char_count / length) * 100
    print(f"{char}: {char_count} occurrences, {percentage:.2f}%")


#=======================================================================================================================

#No.3

import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
string = input("Enter some text: ")
count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

length = len(string)


def draw_graph(char_count, char):

    t2.left(90)
    t2.forward(char_count * 20) 
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(char_count * 20)
    t2.right(90)
    t2.forward(20)
    t2.left(90)
    t2.penup()
    t2.forward(20)
    t2.write(f"{char}", align="left", font=("Arial", 12, "normal"))
    t2.back(20)
    t2.left(90)
    t2.pendown()
    t2.forward(40)

def y_axis():
    max_count = max(count.values())
    t1.penup()
    t1.goto(-200, -150)
    t1.left(180)
    t1.pendown()
    t1.forward(20)
    t1.right(90)
    t1.forward(max_count * 20)

t.Screen()
t.title("Character Frequency Bar Graph")
t.bgcolor("white")
t.setup(800, 400)

t2.penup()
t2.goto(-200, -150)  
t2.pendown()

for char, char_count in count.items():
    draw_graph(char_count, char)
t2.forward(20)
y_axis()

t.exitonclick()

#=======================================================================================================================

#No.4

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