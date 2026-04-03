from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def height(self):
        return self.c

    def squareSurface(self):
        return self.perimetr() * self.c

    def squareBase(self):
        return self.square()

    def volume(self):
        return self.a * self.b * self.c
