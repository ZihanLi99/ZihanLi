# Author: Zihan Li
# Date: 20/11/2019
# Description:  a class named Employee that has data members for 
#               an employee's name, ID_number, salary, and email_address


class Employee:
    def __init__(self, name, ID_number, salary, email):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email = email


def make_employee_dict(names, ID_numbers, salaries, emails):
    employees = {}
    for i in range(len(names)):
        name = names[i]
        ID_number = ID_numbers[i]
        salary = salaries[i]
        email = emails[i]

        emp = Employee(name, ID_number, salary, email)
        employees[ID_number] = emp
    return employees
