from Figure import Figure

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return 2

    def perimetr(self):
        return self.a * 2 + self.b * 2

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()