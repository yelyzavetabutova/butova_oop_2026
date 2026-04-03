class Figure:
    def dimension(self):
        return None
    def perimetr(self):
        if self.dimension() == 3:
            return None
        return 0
    def square(self):
        if self.dimension() == 3:
            return None
        return 0
    def squareSurface(self):
        if self.dimension() == 2:
            return None
        return 0
    def squareBase(self):
        if self.dimension() == 2:
            return None
        return 0
    def height(self):
        if self.dimension() == 2:
            return None
        return 0
    def volume(self):
        if self.dimension() == 2:
            return self.square()
        elif self.dimension() == 3:
            return 0.0
        return None