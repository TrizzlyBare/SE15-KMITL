#No.1

t = input("Please enter the time in 24-hour format (hh:mm): ")

def time_change(time):
    hr, min = time.split(':')
    if int(hr) < 24 and int(hr) >= 0:
        if int(min) < 60 and int(min) >= 0:
            if int(hr) > 12:
                return str(int(hr) - 12) + ':' + min + ' PM'
            elif int(hr) == 0:
                return str(int(hr) + 12) + ':' + min + ' AM'
            elif int(hr) == 12:
                return str(int(hr)) + ':' + min + ' PM'
            else:
                return str(int(hr)) + ':' + min + ' AM'
        else:
            return 'Invalid input of minutes'
    else: 
        return 'Invalid input of hours'
    
print(time_change(t))

#=================================================================================

#No.2

import turtle as t
import calendar
import datetime

def draw_calendar(month_num):
    t.speed(0)

    screen = t.Screen()
    screen.setup(700, 500)

    t.penup()

    now = datetime.datetime.now()
    year = now.year
    month_names = calendar.month_name[month_num]
    cal = calendar.monthcalendar(year, month_num)
    calendar.setfirstweekday(calendar.SUNDAY)

    start_x = -250
    start_y = 100

    t.goto(start_x + 150, start_y + 50)
    t.write(month_names + " " + str(year), align="center", font=("Arial", 18, "bold"))

    day_name = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    for i, days in enumerate(day_name):
        t.goto(start_x + i * 50, start_y)
        t.write(days, align="center", font=("Arial", 14, "normal"))

    for week in cal:
        for days in week:
            if days == 0:
                t.goto(t.xcor() + 50, t.ycor())
            else:
                day_index = (week.index(days) + day_name.index("Mo")) % 7
                t.goto(start_x + day_index * 50, start_y - (cal.index(week) + 1) * 50)
                t.write(str(days), align="center", font=("Arial", 14, "normal"))

    # Draw grid lines
    t.penup()
    t.goto(start_x - 25, start_y + 50)
    t.pendown()
    t.forward(7 * 50)
    t.penup()

    if month_num in [1, 7, 10]:
        for i in range(0, 7):
            t.goto(start_x - 25, start_y - i * 50)
            t.pendown()
            t.forward(7 * 50)
            t.penup()

        for i in range(0, 8):
            t.goto(start_x + i * 50 - 25, start_y + 50)
            t.pendown()
            t.setheading(270)
            t.forward(7 * 50)
            t.penup()

        t.pendown()
        t.back(400)
        t.right(90)
        t.fd(350)
        t.left(90)
        t.fd(50)
    else:
        for i in range(0, 6):
            t.goto(start_x - 25, start_y - i * 50)
            t.pendown()
            t.forward(7 * 50)
            t.penup()

        for i in range(0, 8):
            t.goto(start_x + i * 50 - 25, start_y + 50)
            t.pendown()
            t.setheading(270)
            t.forward(6 * 50)
            t.penup()

        t.pendown()
        t.back(350)
        t.right(90)
        t.fd(350)
        t.left(90)
        t.fd(50)

    t.exitonclick()

def main():
    month_num = int(input("Enter the month number: "))
    draw_calendar(month_num)

main()

#==============================================================================

#No.3

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

#==============================================================================

#No.4

money = int(input("Input your amount of money: "))
moneytypes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

for moneytype in moneytypes:
    if money >= moneytype:
        num = money // moneytype
        if money >= 20:
            print(str(moneytype) + "-Baht notes: " + str(num))
            money = money - num * moneytype
        else:
            print(str(moneytype) + "-Baht coins: " + str(num))
            money = money - num * moneytype

#==============================================================================

#No.5

def reverse_num(num):
    str_num = str(num)
    reverse_str_num = str_num[::-1]
    reverse_num = int(reverse_str_num)
    return reverse_num

print(reverse_num(8375))
