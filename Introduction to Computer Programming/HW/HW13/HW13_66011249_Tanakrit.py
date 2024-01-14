#No.1

def print_btree(tree, depth):
    if not tree:
        return

    node = tree[0]
    left_subtree = tree[1]
    right_subtree = tree[2]

    print("." * depth + str(node))

    if left_subtree:
        print_btree(left_subtree, depth + 1)
    if right_subtree:
        print_btree(right_subtree, depth + 1)

tree = [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]]
print_btree(tree, 2)

#No.2

def display_f(n):
    if n == 0:
        print(f'f({n}) = 0')
        return 0
    elif n % 2 == 0:
        previous_value = display_f(n // 2)
        result = 2 * previous_value + 1
        print(f'f({n}) = {result}')
        return result
    else:
        print(f'f({n}) = 0')
        return 0

display_f(100)

#No.3
def perm2(t, current=[]):
    if len(current) == 2:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm2(t[:i] + t[i+1:], current + [t[i]])

t = [1, 2, 3]
perm2(t)

def perm3(t, current=[]):
    if len(current) == 3:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm3(t[:i] + t[i+1:], current + [t[i]])

t = [1, 2, 3, 4]
perm3(t)

def perm(t, n, current=[]):
    if len(current) == n:
        print(current)
        return
    if not t:
        return

    for i in range(len(t)):
        perm(t[:i] + t[i+1:], n, current + [t[i]])

perm((1,2,3,4), 4)

#No.4

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

#No.5

#Write a program to display a recursive tree

import turtle as t 

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t.speed(0)
    myWin = t.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(75,t)
    myWin.exitonclick()

main()