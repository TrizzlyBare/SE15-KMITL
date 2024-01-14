import turtle as t 

x = int(input("Enter the number : "))

def square(x) :
    for i in range(4):
        t.fd(x)
        t.left(90)

def square_spiral(x):
    for i in range (4):
        for j in range(5):
            square(x * j)
        t.left(90)

square_spiral(x)


t.done()