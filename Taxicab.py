# Author: Zihan Li
# Date: 30/10/2019
# Description: a class named Taxicab that has three private data members: one that holds the current x-coordinate, one
#              that holds the current y-coordinate, and one that holds the odometer reading

class Taxicab:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.odometer = 0

    def get_x_coord(self):
        return self.X

    def get_y_coord(self):
        return self.Y

    def move_x(self, mX):
        self.X += mX
        self.odometer += abs(mX)

    def move_y(self, mY):
        self.Y += mY
        self.odometer += abs(mY)

    def get_odometer(self):
        return self.odometer
