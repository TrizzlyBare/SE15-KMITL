import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
string = [1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4]
count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

length = len(string)

sorted_count = {}
while count:
    min_key = min(count)
    sorted_count[min_key] = count.pop(min_key)

print(sorted_count)

def draw_graph(char_count, char):
    t2.left(90)
    t2.begin_fill()
    t2.forward(char_count * 20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(char_count * 20)
    t2.right(90)
    t2.forward(20)
    t2.end_fill() 
    t2.left(90)
    t2.penup()
    t2.forward(20)
    t2.write(f"{char}", align="left", font=("Arial", 12, "normal"))
    t2.back(20)
    t2.left(90)
    t2.pendown()
    t2.forward(20)

def y_axis():
    max_count = max(sorted_count.values())
    t1.penup()
    t1.goto(-200, -150)
    t1.left(180)
    t1.pendown()
    t1.forward(20)
    t1.right(90)
    t1.forward(max_count * 20)
    t1.write("Y")

t.Screen()
t.title("Character Frequency Bar Graph")
t.bgcolor("white")
t.setup(800, 400)

t2.penup()
t2.goto(-200, -150)
t2.pendown()

for char, char_count in sorted_count.items():
    draw_graph(char_count, char)
t2.forward(20)
t2.write("X")

y_axis()

t1.hideturtle()
t2.hideturtle()

t.exitonclick()
