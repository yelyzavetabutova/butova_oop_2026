from lab_5.Rational import Rational
class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        self.message = message
        super().__init__(self.message)

class NewRational(Rational):
    def __init__(self, *args):
        super().__init__(*args)
        if self.d == 0:
            raise RationalError("Denominator cannot be zero")

if __name__ == '__main__':
    m = NewRational(7,0) #тест, воно працює :)
