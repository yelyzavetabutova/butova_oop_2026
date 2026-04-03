from Ball import *
from Triangle import *
from Rectangle import *
from Trapeze import *
from Parallelogram import *
from Circle import *
from TriangularPyramid import *
from QuadrangularPyramid import *
from Cone import *
from TriangularPrism import *
from RectangularParallelepiped import *

def get_measure(shape):
    return shape.volume()

out = open('output.txt', 'w')

for i in range(1, 4):
    filename = f"input0{i}.txt"
    shapes = []

    file = open(filename, 'r')
    for line in file:
        parts = line.split()
        if not parts: continue

        name, params = parts[0], [float(x) for x in parts[1:]]

        if name == "Triangle":
            shapes.append(Triangle(*params))
        elif name == "Rectangle":
            shapes.append(Rectangle(*params))
        elif name == "Trapeze":
            shapes.append(Trapeze(*params))
        elif name == "Parallelogram":
            shapes.append(Parallelogram(*params))
        elif name == "Circle":
            shapes.append(Circle(*params))
        elif name == "Ball":
            shapes.append(Ball(*params))
        elif name == "TriangularPyramid":
            shapes.append(TriangularPyramid(*params))
        elif name == "QuadrangularPyramid":
            shapes.append(QuadrangularPyramid(*params))
        elif name == "RectangularParallelepiped":
            shapes.append(RectangularParallelepiped(*params))
        elif name == "Cone":
            shapes.append(Cone(*params))
        elif name == "TriangularPrism":
            shapes.append(TriangularPrism(*params))

    file.close()

    if shapes:
        best = max(shapes, key=get_measure)
        out.write(f"File {filename}: Max measure = {best.volume():.2f} ({type(best).__name__})\n")

out.close()
