# Author: Zihan Li
# Date: 2020/2/25
# Description: a decorator function named sort_timer that times how many seconds it takes the decorated function to run

import random
import time

from matplotlib import pyplot

def sort_timer(func):
    def func_wrapper(lst):
    # decorator function for sort algorithm
        a = time.perf_counter()
        # wrapper function
        func(lst)
        # execute sort function
        b = time.perf_counter()
        return b - a
        # return time duration
    return func_wrapper

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

def compare_sort(sort1, sort2):
    m1 = sort_timer(sort1)
    m2 = sort_timer(sort2)
    # decorated sort algorithms

    times1 = []
    times2 = []
    counts = []

    for count in range(2000, 11000, 1000):
    # loop from 2000 3000 4000 ... 10000
        lst = [random.randint(0, 10000) for i in range(count)]
        lst1 = list(lst)
        lst2 = list(lst)
        # generate data

        dt1 = m1(lst1)
        dt2 = m2(lst2)
        # calculate duration

        counts.append(count)
        times1.append(dt1)
        times2.append(dt2)
        # add to result
        print('count = {} finished.'.format(count))

    pyplot.plot(counts, times1, 'ro--', linewidth=2)
    pyplot.plot(counts, times2, 'go--', linewidth=2)
    # plot data
    pyplot.show()
