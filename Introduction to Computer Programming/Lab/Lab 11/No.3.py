class Name:
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last    
       
    def setName(self, t, f, l):
        self.title = t
        self.first = f
        self.last = l
    
    def getFullName(self):
        return f"{self.title} {self.first} {self.last}"

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    
    def getDate(self):
        if 1 <= self.day <= 31 and 1 <= self.month <= 12:
            return f"{self.day}/{self.month}/{self.year}"
        else:
            return "Invalid date"
    
    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year + 543}"

class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    
    def setAddress(self, h, s, d, c, co, p):
        self.houseNo = h
        self.street = s
        self.district = d
        self.city = c
        self.country = co
        self.postcode = p

    def getAddress(self):
        return f"{self.houseNo} {self.street} {self.district} {self.city} {self.country} {self.postcode}"
    
class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList

    def addEmployee(self, employee):
        self.employeeList.append(employee)
        employee.department = self
    
    def deleteEmployee(self, employee):
        self.employeeList.remove(employee)
        employee.department = None

    def setManager(self, manager):
        self.manager = manager

    def printInfo(self):
        print(f"Department: {self.description}")
        print(f"Manager: {self.manager.getFullName()}")
        print("Employees:")
        for employee in self.employeeList:
            print(f"  {employee.name.getFullName()}")

class Person:
    def __init__(self, name, dateBirth, address):
        self.name = name
        self.dateBirth = dateBirth
        self.address = address

    def printInfo(self):
        print(f"Name: {self.name.getFullName()}")
        print(f"Date of Birth: {self.dateBirth.getDate()}")
        print(f"Address: {self.address.getAddress()}")

class Employee(Person):
    def __init__(self, name, dateBirth, address, startDate, department):
        super().__init__(name, dateBirth, address)
        self.startDate = startDate
        self.department = department
    
    def printInfo(self):
        super().printInfo()
        print(f"Start Date: {self.startDate.getDate()}")
        print(f"Department: {self.department.description}")

class TempEmployee(Employee):
    def __init__(self, name, dateBirth, address, startDate, department, wage):
        super().__init__(name, dateBirth, address, startDate, department)
        self.wage = wage
    
    def printInfo(self):
        super().printInfo()
        print(f"Wage: {self.wage}")

class PermEmployee(Employee):
    def __init__(self, name, dateBirth, address, startDate, department, salary):
        super().__init__(name, dateBirth, address, startDate, department)
        self.salary = salary
    
    def printInfo(self):
        super().printInfo()
        print(f"Salary: {self.salary}")

name = Name("Mr", "John", "Doe")
birthdate = Date(10, 5, 1990)
address = Address("123", "Main St", "Central", "City", "Country", "12345")
department = Department("HR Department", None, [])

employee = PermEmployee(name, birthdate, address, birthdate, department, 50000)

print("Employee Information:")
employee.printInfo()
