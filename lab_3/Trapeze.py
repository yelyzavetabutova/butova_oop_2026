from Figure import Figure
import math

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimension(self):
        return 2

    def perimetr(self):
        return self.a+self.b+self.c+self.d

    def square(self):
        if self.a == self.b: return 0.0
        d = 4 * abs(self.a - self.b)
        term1 = -self.a + self.b + self.c + self.d
        term2 = self.a - self.b + self.c + self.d
        term3 = self.a - self.b + self.c - self.d
        term4 = self.a - self.b - self.c + self.d
        root = math.sqrt(abs(term1 * term2 * term3 * term4))
        return ((self.a + self.b) / d) * root

    def volume(self):
        return self.square()