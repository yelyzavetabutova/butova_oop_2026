from lab_5.Rational import Rational
from lab_5.RationalList import RationalList

class RationalValueError(ValueError):
    def __init__(self, message="Wrong data"):
        super().__init__(message)

class NewRationalList(RationalList):
    # Додамо перевірку при заміні елемента через []
    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise RationalValueError("Can only set Rational objects")
        super().__setitem__(index, value)

    def __add__(self, other):
        if not isinstance(other, (RationalList, Rational, int)):
            raise RationalValueError("Wrong data")
        return super().__add__(other)

    def __iadd__(self, other):
        if not isinstance(other, (RationalList, Rational, int)):
            raise RationalValueError("Wrong data")
        return super().__iadd__(other)

if __name__ == "__main__":
    lst = NewRationalList()
    lst += "рядок" # тест ^_^
