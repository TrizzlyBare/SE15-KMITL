import turtle

radius = float(input("Enter the radius of the ring: "))

t = turtle.Turtle()

t.pensize(4)

t.penup()
t.goto(-2.3 * radius, 0)
t.pendown()
t.color("blue")
t.circle(radius)

t.penup()
t.goto(0, 0)
t.pendown()
turtle.color("black")
turtle.circle(radius)

t.penup()
t.goto(2.3 * radius, 0)
t.pendown()
t.color("red")
t.circle(radius)

t.penup()
t.goto(-radius, -radius)
t.pendown()
t.color("yellow")
t.circle(radius)

t.penup()
t.goto(radius, -radius)
t.pendown()
t.color("green")
t.circle(radius)

turtle.done()