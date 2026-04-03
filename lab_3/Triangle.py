from Figure import Figure
import math

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def dimension(self):
        return 2
    def perimeter(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimeter()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def volume(self):
        return self.square()
