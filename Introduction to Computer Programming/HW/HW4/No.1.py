try:
    x_p0 = float(input("Enter the x of point 0: "))
    y_p0 = float(input("Enter the y of point 0: "))
    x_p1 = float(input("Enter the x of point 1: "))
    y_p1 = float(input("Enter the y of point 1: "))
    x_p2 = float(input("Enter the x of point 2: "))
    y_p2 = float(input("Enter the y of point 2: "))

    if x_p0 < x_p2 < x_p1 or x_p1 < x_p2 < x_p0:
        print("Between point 0 and point 1")
    elif x_p2 > x_p0 and x_p2 > x_p1:
        if x_p1 > x_p0:
            print("Point 2 is on the right of point 1")
        else:
            print("Point 2 is on the right of point 0")
    else:
        if x_p1 < x_p0:
            print("Point 2 is on the left of point 1")
        else:
            print("Point 2 is on the left of point 0")

except :
    print("Invalid input.")