mark = int(input("Enter your score: "))

def grade(score):
    if 101 > score >= 80:
        return("A")
    elif score >= 70:
        return("B")
    elif score >= 60:
        return("C")
    elif score >= 50:
        return("D")
    elif score >= 0:
        return("F")

print(f"Your grade is {grade(mark)}.")


