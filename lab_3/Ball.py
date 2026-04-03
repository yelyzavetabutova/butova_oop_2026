from Figure import Figure
import math

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def volume(self):
        return 4/3*math.pi*(self.r**3)

