from Rational import Rational
class RationalList:
    def __init__(self, data=None):
        if data is None:
            self.elements = []
        else:
            if all(isinstance(x, Rational) for x in data):
                self.elements = list(data)
            else:
                raise ValueError("Only Rational")

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self.elements[index] = value
        else:
            raise TypeError("Can't add")

    def __len__(self):
        return len(self.elements)

    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList(self.elements + other.elements)
        elif isinstance(other, (Rational, int)):
            if isinstance(other, Rational):
                new_item = other
            else:
                new_item = Rational(other, 1)
            new_list = self.elements.copy()
            new_list.append(new_item)
            return RationalList(new_list)
        else:
            raise TypeError("Can't add")

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.elements.extend(other.elements)
        elif isinstance(other, (Rational, int)):
            if isinstance(other, Rational):
                new_item = other
            else:
                new_item = Rational(other)
            self.elements.append(new_item)
        else:
            raise TypeError("Can't add")
        return self

filenames = ["input01.txt", "input02.txt", "input03.txt"]
for name in filenames:
    r_list = RationalList()
    with open(name, 'r') as f_input:
        for line in f_input:
            for word in line.split():
                if word in "+-*":
                    continue
                r_list += Rational(word)
    total_sum = Rational(0, 1)
    for r in r_list.elements:
        total_sum = total_sum + r

    output_name = name.replace("input", "output")
    with open(output_name, 'w') as f_output:
        print(f"File: {name}", file=f_output)
        print(f"Sum: {total_sum}", file=f_output)
