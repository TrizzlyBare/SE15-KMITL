try :
    x1 = float(input("Enter the x1 coordinates : "))
    y1 = float(input("Enter the y2 coordinates : "))
    w1 = float(input("Enter the width of rectangle number 1 : "))
    h1 = float(input("Enter the height of rectangle number 1 : "))

    x2 = float(input("Enter the x2 coordinates : "))
    y2 = float(input("Enter the y2 coordinates : "))
    w2 = float(input("Enter the width of rectangle number 2 : "))
    h2 = float(input("Enter the height of rectangle number 2 : "))

    left1 = x1 - (w1 / 2)
    right1 = x1 + (w1 / 2)
    top1 = y1 + (h1 / 2)
    bottom1 = y1 - (h1 / 2)

    left2 = x2 - (w2 / 2)
    right2 = x2 + (w2 / 2)
    top2 = y2 + (h2 / 2)
    bottom2 = y2 - (h2 / 2)

    if left1 >= left2 and right1 <= right2 and top1 <= top2 and bottom1 >= bottom2:
        print("Rectangle number 1 is inside rectangle number 2.")
    elif left2 >= left1 and right2 <= right1 and top2 <= top1 and bottom2 >= bottom1:
        print("Rectangle number 2 is inside rectangle number 1.")
    elif left1 < right2 or right1 > left2 or top1 > bottom2 or bottom1 < top2:
        print("The rectangles are overlap.")
    else :
        print("The rectangles do not overlap.")
except :
    print("Invalid Value")
