from turtle import *

def main():
    reset()
    lt(90)

    begin_poly()
    fd(100)
    rt(90)
    fd(10)
    lt(120)
    fd(20)
    lt(120)
    fd(20)
    lt(120)
    fd(10)
    end_poly()    

    hand = get_poly()

    lt(90)
    bk(100)
    clear()
    pensize(7)

    pu()
    for i in range(12):
        fd(125)
        pd()
        fd(25)
        pu()
        bk(150)
        rt(30)
        
    register_shape("hand", hand)
    shape("hand")
    resizemode("user")
    turtlesize(1, 1, 3)
    color("red", "blue")

    def tick():
        right(6)
        ontimer(tick, 1000)

    speed(1)
    ontimer(tick, 1000)
    return "EVENTLOOP"

if __name__ == '__main__':
    main()
    mainloop()   
