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
    t.hideturtle()

def main():
    month_num = int(input("Enter the month number: "))
    draw_calendar(month_num)

main()
