from lab_5.Rational import Rational

class RationalValueError(ValueError):
    def __init__(self, messege = "Incorrect data"):
        self.messege = messege
        super().__init__(self.messege)

class NewRational(Rational):
    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError
        return super().__add__(other)

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError
        return super().__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError
        return super().__mul__(other)

if __name__ == '__main__':
    r = NewRational(1, 3)
    res = r + "рядок" # працює :3
