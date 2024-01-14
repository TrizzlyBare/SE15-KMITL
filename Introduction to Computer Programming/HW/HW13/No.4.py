#Write a recursive program to solve the tower of Hanoi and draw an animation of it.

import turtle as t

t.setpos(-400, 0)

def hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", c)
        return
    hanoi(n-1, a, c, b)
    print("Move disk", n, "from", a, "to", c)
    hanoi(n-1, b, a, c)

def draw_hanoi(n, a, b, c):
    if n == 1:
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        return
    draw_hanoi(n-1, a, c, b)
    draw_hanoi(n-1, b, a, c)
    draw_hanoi(n-1, a, c, b)

def main():
    hanoi(3, "A", "B", "C")
    print(hanoi(3, "A", "B", "C"))
    draw_hanoi(3, "A", "B", "C")
    myWin = t.Screen()
    myWin.exitonclick()

main()