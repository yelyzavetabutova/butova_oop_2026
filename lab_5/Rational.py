import math

class Rational:
    def __init__(self, *args):
        if len(args) == 2:
            n, d = args
        elif len(args) == 1 and isinstance(args[0], str):
            if '/' in args[0]:
                parts = args[0].split('/')
                n, d = int(parts[0]), int(parts[1])
            else:
                n, d = int(args[0]), 1
        elif len(args) == 1 and isinstance(args[0], Rational):
            n, d = args[0].n, args[0].d
        else:
            raise ValueError("Wrong arguments")
        common = math.gcd(n, d)
        self.n = n // common
        self.d = d // common

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.n * other.n, self.d * other.d)

def solve_expression(expression):
    elem = expression.split()
    new_ex = []
    for t in elem:
        if t in "+-*":
            new_ex.append(t)
        else:
            new_ex.append(f"Rational('{t}')")
    expressions = " ".join(new_ex)
    return eval(expressions)

with open('input1.txt', 'r') as file_input, open('output_1.txt', 'w') as file_output:
    for line in file_input:
        line = line.strip()
        if line:
            result = solve_expression(line)
            print(f"Expression: {line}", file=file_output)
            print(f"Result: {result}", file=file_output)

