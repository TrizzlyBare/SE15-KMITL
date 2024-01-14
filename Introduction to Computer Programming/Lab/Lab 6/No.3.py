import turtle as t 

def draw_polygon(x, y, side = 4, size = 100):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(side):
        t.forward(size)
        t.left(360/side)
    t.penup()

draw_polygon(10,10,5,200)

t.done()