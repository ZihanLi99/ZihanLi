# Author: Zihan Li
# Date: 2020/1/29
# Description: a Box class whose init method takes three parameters and uses them to
#              initialize the length, width and height of a Box

from math import floor
class TargetNotFound(Exception):
    pass

def bin_except(arr, tar_val):
    min = 0
    max = len(min) - 1
    while min <= max:
        mid = floor((min + max) / 2)
        if arr[mid] == tar_val:
            return mid
        if arr[mid] > tar_val:
            max = mid - 1
        else:
            min = mid + 1
    raise TargetNotFound("Can't find the number.")
