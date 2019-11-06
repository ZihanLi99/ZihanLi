# Author: Zihan Li
# Date: 5/11/2019
# Description: a function use a list comprehension to return a list that contains only those names that start with
#              a "K", but with the surname "Kardashian" added to each one


def add_surname(name_list):
    return [f_name + " Kardashian" for f_name in name_list if f_name[0].upper() == 'K']
