#Define a recursive function to draw a cross

import turtle as t

def draw_cross(size, depth):
    if depth == 0:
        t.dot(5)
    else:
        for _ in range(4):
            t.forward(size)
            draw_cross(size / 2, depth - 1)
            t.backward(size)
            t.right(90)

t.speed(0)
draw_cross(100, 4)
t.mainloop()