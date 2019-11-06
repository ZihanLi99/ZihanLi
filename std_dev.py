# Author: Zihan Li
# Date: 5/11/2019
# Description: a separate function called std_dev that takes as a parameter a list of
#              Person objects and returns the standard deviation of all their ages

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def std_dev(person_list):
    if len(person_list) == 0:
        return 0

    age_sum = 0
    for person in person_list:
        age_sum += person.age
    age_avg = age_sum / len(person_list)

    t = 0
    for person in person_list:
        t += (person.age-age_avg) ** 2
    std = t / len(person_list)
    return std ** 0.5
