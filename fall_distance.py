# Author: Zihan Li
# Date: 22/10/2019
# Description: determine the distance an object falls due to gravity in a specific time period

def fall_distance(t):
    d = (1/2) * 9.8 * t ** 2
    return d


# print("Enter t:")
# t = float(input())
# print(fall_distance(t))
