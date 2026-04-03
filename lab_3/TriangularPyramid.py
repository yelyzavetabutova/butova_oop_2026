from Triangle import Triangle
import math

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return 3

    def height(self):
        return self.h

    def squareSurface(self):
        r = self.a / (2 * math.sqrt(3))
        l_apothema = math.sqrt(self.h ** 2 + r ** 2)
        return 0.5 * self.perimetr() * l_apothema

    def squareBase(self):
        return self.square()

    def volume(self):
        return 1/3*self.squareBase()*self.h