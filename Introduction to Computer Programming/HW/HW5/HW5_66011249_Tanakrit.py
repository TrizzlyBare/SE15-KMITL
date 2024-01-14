#No.1
n = float(input("Please enter your number : "))

guess = n / 2.0
for _ in range(0, 5) :
    temp = n / guess 
    guess = (guess + temp) / 2.0
    approx_5_iter = round(guess, 3)

guess = n / 2.0
for _ in range(0, 6) :
    temp = n / guess
    guess = (guess + temp) / 2.0
    approx_6_iter = round(guess,3)

guess = n / 2.0
for _ in range(0, 7) :
    temp = n / guess
    guess = (guess + temp) / 2.0
    approx_7_iter = round(guess,3)

print ("5 iterations", approx_5_iter)
print ("6 iterations", approx_6_iter)
print ("7 iterations", approx_7_iter)

#No.2
import turtle as t

win_width, win_height, bg_color = 5000, 5000, 'white'

t.setup()
t.screensize(win_width, win_height, bg_color)

t.tracer(0)
t.penup()
t.goto(-500, 400)
t.pendown()

day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
monthR = [5, 5, 5, 6, 5, 5, 6, 5, 5, 5, 5, 6]
monthS = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
monthEnd = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

month = 0
column = 0

while column < 3:
    row = 0
    while row < 4:
        t.pencolor("black")
        t.fillcolor("white")
        t.begin_fill()
        i = 0
        while i < 2:
            t.forward(245)
            t.right(90)
            t.forward(25)
            t.right(90)
            i += 1
        t.end_fill()
        t.right(90)
        t.forward(25)
        t.left(90)
        t.write(f"  Month#{month + 1}", font=("Arial", 14))
        
        i = 0
        while i < 7:
            j = 0
            while j < 2:
                t.forward((200 // 7) + 7)
                t.right(90)
                t.forward(25)
                t.right(90)
                j += 1
            t.forward((200 // 7) + 7)
            i += 1
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(245)
        t.right(180)
        for d in day:
            t.write(f" {d}", font=("Arial", 14))
            t.forward((200 // 7) + 7)
        t.right(180)
        t.forward(245)
        t.right(180)
        
        i = 0
        while i < monthR[month]:
            j = 0
            while j < 7:
                k = 0
                while k < 2:
                    t.forward((200 // 7) + 7)
                    t.right(90)
                    t.forward(25)
                    t.right(90)
                    k += 1
                day_num = j + 1 + (7 * i) + monthS[month]
                if monthS[month] <= day_num < monthEnd[month]:
                    t.write(f" {day_num}", font=("Arial", 14))
                else:
                    t.write("    ", font=("Arial", 14))  # Empty space if no date
                t.forward((200 // 7) + 7)
                j += 1
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(245)
            t.right(180)
            i += 1  
            
        month += 1
        t.penup()
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(245)
        t.right(180)
        t.pendown()
        row += 1
        
    t.penup()
    t.goto(-500 + 400 * (column + 1), 400)
    t.pendown()
    column += 1

t.done()

#No.3
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

