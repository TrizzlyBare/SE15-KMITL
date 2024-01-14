import math

x1 = float(input("x point 1 coordinates: "))
x2 = float(input("x point 2 coordinates: "))
x3 = float(input("x point 3 coordinates: "))
y1 = float(input("y point 1 coordinates: "))
y2 = float(input("y point 2 coordinates: "))
y3 = float(input("y point 3 coordinates: "))
x_avg = (x1+x2+x3)/3
lowest_y = min(y1,y2,y3)

area = (1/2) * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

print("The area of the triangle is:", area)

import turtle

t = turtle.Turtle()

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)
t.penup()

t.goto(x_avg, lowest_y-20)
t.write("Area: {:.2f}".format(area))

turtle.done()