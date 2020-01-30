# Author: Zihan Li
# Date: 2020/1/29
# Description: a Box class whose init method takes three parameters and uses them to
#              initialize the length, width and height of a Box

class Box:
    def __init__(self, length, width, height):
        self.length = length
        # the length of box
        self.width = width
        # the width of box
        self.height = height
        # the height of box
    def getVolume(self):
        return self.length * self.width * self.height
        # the function of box's volume

def box_sort(box_list):
    for b in range(1, len(box_list)):
        temp = box_list[b]
        B = b-1
        while B >= 0 and temp.getVolume() > box_list[B].getVolume() :
            box_list[B+1] = box_list[B]
            B -= 1
        box_list[B+1] = temp
        # insertion sort from greatest volume to least volume
    return box_list
