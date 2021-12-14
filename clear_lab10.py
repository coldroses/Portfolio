#paul clear  status: complete

import employee

#create same number of instances of the class employee and add them to a list
#for each employee, program gets info form user, passed on as parameter to init meth
#then collects salary change (increase or decrease) info from user
#for each employee and pass it as parameter to either increase_salary
#or decrease_salary methods
#at end, program should use __str__ method to display information for all new
#employees

#hint: pp 513, 514, 516, 517, 523 as ref.
#instead of using printing in cellphone class, invoke __str__ in main func

def main():

    emp = empList()


    #salDiff = int(input('Salary change for ', employee.name,'(negative if decreased):'))
        

    #name.Employee
    #idNumber.Employee
    #department.Employee
    #position.Employee
    #salary.Employee

def empList():
    #create empty list
    empList = []

    #ask user to enter number of new employees
    count = 0
    newEmp = int(input('Enter number of new employees: '))

    for count in range (0, newEmp):
        print("Employee: ", count+1)
        name = input('Enter employee name: ')
        idNumber = input('Enter employee ID: ')
        department = input('Enter department: ')
        jobTitle = input('Enter position: ')
        salary = int(input('Enter initial salary: '))

        empData = employee.Employee(name, idNumber, department, jobTitle, salary)
##        print(empData)
        empList.append(empData)

    for e in empList:
        print(e)

        
    for e in empList:
        amount = int(input("Salary change for " + e.get_name() + " (negative if decreased):"))
        if amount > 0:
            e.increase_salary(amount)
        else:
            e.decrease_salary(-amount)

    for e in empList:
        print(e)
        


main()

#output/sample dialog
#employee 1:
#Enter employee name: Mary Smith
#Enter employee ID: 123456
#Enter department: Accounting
#Enter position: Accountant
#Enter initial salary: 50000

#Employee 2:
#Enter employee name: Joe Morales
#Enter employee ID: 678910
#Enter department: Engineering
#Enter position: Engineer
#Enter initial salary: 80000

#Salary change for Mary Smith (negative if decreased): -3000
#Salary change for Joe Morales (negative if decreased): 4000

#employee 1:
#Enter employee name: Mary Smith
#Enter employee ID: 123456
#Enter department: Accounting
#Enter position: Accountant
#Enter new salary: 47000

#Employee 2:
#Enter employee name: Joe Morales
#Enter employee ID: 678910
#Enter department: Engineering
#Enter position: Engineer
#Enter new salary: 84000
