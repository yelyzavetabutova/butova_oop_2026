from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return 3

    def height(self):
        return self.h

    def squareSurface(self):
        return self.perimetr() * self.h

    def squareBase(self):
        return self.square()

    def volume(self):
        return self.squareBase() * self.h

