import turtle

radius = int(input("Enter the radius :"))
centerx = int(input("x"))
centery = int(input("y"))
area = radius * radius * 3.14

turtle.penup()
turtle.goto(centerx, centery)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(centerx, centery + radius)
turtle.pendown()
turtle.write(area)

turtle.done()