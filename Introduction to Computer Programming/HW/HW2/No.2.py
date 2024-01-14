import turtle 

t=turtle.Turtle()

t.penup()
t.goto(-200,-200)
t.pendown()

t.fd(400)
t.left(90)
t.fd(200)
t.left(90)
t.fd(400)
t.left(90)
t.fd(200)
#rectangle

t.penup()
t.goto(-200,0)
t.pendown()

t.left(150)
t.fd(100)
t.right(120)
t.fd(100)
#triangle

t.right(30)
t.fd(200)

t.penup()
t.goto(200,0)
t.pendown()

t.right(150)
t.fd(100)
t.left(60)
t.fd(300)
#roof

t.penup()
t.goto(-170,-200)
t.pendown()

t.right(90)
t.fd(70)
t.right(90)
t.fd(40)
t.right(90)
t.fd(70)
#door

t.penup()
t.goto(-170,-90)
t.pendown()

t.left(90)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)

t.penup()
t.goto(-150,-90)
t.pendown()

t.left(180)
t.fd(40)

t.penup()
t.goto(-170,-70)
t.pendown()

t.right(90)
t.fd(40)
#window1

t.penup()
t.goto(-10,-90)
t.pendown()

t.left(90)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)

t.penup()
t.goto(-30,-90)
t.pendown()

t.left(90)
t.fd(40)

t.penup()
t.goto(-10,-70)
t.pendown()

t.left(90)
t.fd(40)
#window2

t.penup()
t.goto(70,-90)
t.pendown()

t.left(180)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)
t.left(90)
t.fd(40)

t.penup()
t.goto(90,-90)
t.pendown()

t.left(180)
t.fd(40)

t.penup()
t.goto(70,-70)
t.pendown()

t.right(90)
t.fd(40)

t.penup()
t.goto(-200,-200)
t.pendown()

turtle.done()