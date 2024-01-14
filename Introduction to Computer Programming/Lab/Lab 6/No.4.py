def sum_of_all_digit(number) :
    sum = 0
    for i in number :
        sum += int(i)
    return sum

num = input("Enter a number : ")
print("Sum of all digit of is", sum_of_all_digit(num))