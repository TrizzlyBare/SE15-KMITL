# No.1
import math
employee = str(input("Enter employee's name :"))
hours = float(input("Enter number of hours worked in a week :"))
pay_rate = float(input("Enter hourly pay rate :"))
federal_tax = float(input("Enter federal tax withholding rate :"))
state_tax = float(input("Enter state tax withholding rate :"))

gross_pay = hours*pay_rate
federal_withholding = federal_tax * gross_pay
state_withholding = state_tax * gross_pay
total_deduction = federal_withholding+state_withholding
net_pay = gross_pay - total_deduction

print ("Employee Name :", employee)
print ("Hours Worked:", format(hours, ".1f"))
print ("Pay Rate: $" + format(pay_rate, '.2f'))
print ("Gross Pay: $" + format(gross_pay, '.2f'))
print ("Deductions:\n",
       "Federal Withholding (" + format(federal_tax * 100, '.1f') + "%): $" + format(federal_withholding, '.2f') + "\n",
       "State Withholding(" + format(state_tax * 100, '.1f') + "%) :  $" + str(math.floor(state_withholding * 10 ** 2) / 10 ** 2) + "\n",
       "Total Deduction : $" + format(total_deduction, '.2f'))
print ("Net Pay : $" + format(net_pay, '.2f'))

#No.2
integer = int(input("4 digit number :"))

three_digit = integer % 1000
two_digit = integer % 100

num_4 = integer // 1000
num_3 = three_digit // 100
num_2 = two_digit//10
num_1 = two_digit%10

print(str(num_1)+str(num_2)+str(num_3)+str(num_4))

#No.3
Length = int(input("Length of star :"))

import turtle

t = turtle.Turtle()

t.penup()
t.goto(-120,-120)
t.left(70)
t.pendown()

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)
t.right(144)

t.fd(Length)

turtle.done()

#No.4
import math

x1 = float(input("x point 1 coordinates: "))
x2 = float(input("x point 2 coordinates: "))
x3 = float(input("x point 3 coordinates: "))
y1 = float(input("y point 1 coordinates: "))
y2 = float(input("y point 2 coordinates: "))
y3 = float(input("y point 3 coordinates: "))
x_avg = (x1+x2+x3)/3
lowest_y = min(y1,y2,y3)

area = (1/2) * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

print("The area of the triangle is:", area)

import turtle

t = turtle.Turtle()

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)
t.penup()

t.goto(x_avg, lowest_y-20)
t.write("Area: {:.2f}".format(area))

turtle.done()

#No.5
import math

x1 = float(input("x point 1 coordinates: "))
x2 = float(input("x point 2 coordinates: "))
x3 = float(input("x point 3 coordinates: "))
y1 = float(input("y point 1 coordinates: "))
y2 = float(input("y point 2 coordinates: "))
y3 = float(input("y point 3 coordinates: "))
x_avg = (x1+x2+x3)/3
lowest_y = min(y1,y2,y3)

area = (1/2) * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

print("The area of the triangle is:", area)

import turtle

t = turtle.Turtle()

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)
t.penup()

t.goto(x_avg, lowest_y-20)
t.write("Area: {:.2f}".format(area))

turtle.done()