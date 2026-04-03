from Rectangle import Rectangle
import math

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimension(self):
        return 3

    def height(self):
        return self.h

    def squareSurface(self):
        l_apothema = math.sqrt(self.h ** 2 + (self.a / 2) ** 2)
        return 2 * self.a * l_apothema

    def squareBase(self):
        return self.square()

    def volume(self):
        return 1/3*self.h*self.squareBase()
