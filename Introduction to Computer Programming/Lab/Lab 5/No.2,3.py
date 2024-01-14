import turtle

N = int(input("Enter the frequent of the table: "))

t = turtle
fb = 100 / N

# for i in range(4):
#     t.fd(100)
#     t.left(90)

for a in range(N):
    for i in range(N):
         if (a % 2 == 0 and i % 2 == 0) or (a % 2 == 1 and i % 2 == 1):
            t.fillcolor("Black")
            t.begin_fill()
            for j in range(4):
                t.fd(fb)
                t.left(90)    
         else:
              for j in range(4):
                t.fd(fb)
                t.left(90)  
         t.end_fill()
         t.fd(fb)
    t.left(90)
    t.fd(fb)
    t.left(90)
    t.fd(100)
    t.right(180)