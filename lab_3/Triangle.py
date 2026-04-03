from Figure import Figure
import math

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def dimension(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimetr()/2
        return math.sqrt(abs(p * (p - self.a) * (p - self.b) * (p - self.c)))
    def volume(self):
        return self.square()
