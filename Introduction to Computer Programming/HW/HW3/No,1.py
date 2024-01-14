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

