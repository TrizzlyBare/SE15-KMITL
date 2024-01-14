Length = int(input("Length of star :"))

import turtle

t = turtle.Turtle()

t.penup()
t.goto(-120,-120)
t.left(70)
t.pendown()

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)

turtle.done()