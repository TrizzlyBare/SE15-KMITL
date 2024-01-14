integer = int(input("4 digit number :"))

three_digit = integer % 1000
two_digit = integer % 100

num_4 = integer // 1000
num_3 = three_digit // 100
num_2 = two_digit//10
num_1 = two_digit%10

print(str(num_1)+str(num_2)+str(num_3)+str(num_4))

