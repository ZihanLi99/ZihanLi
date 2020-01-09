# Author: Zihan Li
# Date: 2020/1/8
# Description:   a class called Person that has two data members - the person's name and age. It should
#                have an init method that takes two values and uses them to initialize the data members

import statistics

class Person:
    """
    Represents a person. Contains methods for getting name and age.
    """

    def __init__(self, name, age):
        """
        Returns a Person with the given age and name.
        """
        self.name = name
        self.age = age

def basic_stats(person_list):
    """
    Returns a tuple containing the mean, median, and mode of these ages.
    """

    age = []  # create list to store ages from person_li

    for p_l in person_list:  # a for loop for getting age from each person
        age.append(p_l.age)

    mean_age = statistics.mean(age)  # get mean of ages

    median_age = statistics.median(age)  # get median of ages

    mode_age = statistics.mode(age)  # get mode of ages

    return mean_age, median_age, mode_age  # returns mean, median, mode
