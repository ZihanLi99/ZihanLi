# Author: Zihan Li
# Date: 20/11/2019
# Description:  a class named Employee that has data members for 
#               an employee's name, ID_number, salary, and email_address


class Employee:
    def __init__(self, name, id, salary, email):
        self.name = name
        self.id = id
        self.salary = salary
        self.email = email


def make_employee_dict(names, ids, salaries, emails):
    employees = {}
    for i in range(len(names)):
        name = names[i]
        id = ids[i]
        salary = salaries[i]
        email = emails[i]

        emp = Employee(name, id, salary, email)
        employees[id] = emp
    return employees
