from Figure import Figure
import math

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return math.pi*self.r*2

    def square(self):
        return math.pi*(self.r**2)

    def volume(self):
        return self.square()