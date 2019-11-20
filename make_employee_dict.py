# Author: Zihan Li
# Date: 20/11/2019
# Description:  a class named Employee that has data members for 
#               an employee's name, ID_number, salary, and email_address


class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address


def make_employee_dict(names, ID_numbers, salaries, email_addresses):
    employees = {}
    for i in range(len(names)):
        name = names[i]
        ID_number = ID_numbers[i]
        salary = salaries[i]
        email_address = email_addresses[i]

        emp = Employee(name, ID_number, salary, email_address)
        employees[ID_number] = emp
    return employees
