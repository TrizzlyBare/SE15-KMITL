import turtle as t

N = int(input("Please input numbers of N = "))

scr = t.Screen()  

n = 100/N

def draw():
    t.down
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    
if __name__=="__main__":
    scr.setup(500,700)
    t.speed(50)
    
    for line in range(N):
    
        for x in range(N):
            if (line % 2 == 0 and x % 2 == 0) or (line % 2 == 1 and x % 2 == 1):
                t.begin_fill()
                draw()
                t.end_fill()
            else:
                draw()
        t.right(90)
        t.forward(n)
        t.right(90)
        t.forward(100)
        t.right(180)
t.done()