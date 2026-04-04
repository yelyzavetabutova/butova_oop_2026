import turtle
class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

    def draw(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.setheading(self.angle)
        self.t.pendown()
        self._render()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.draw()

    def rotate(self, d_angle):
        self.angle += d_angle
        self.draw()

class Petal:
    def draw(self, t, color):
        t.color(color)
        t.begin_fill()
        t.circle(20)
        t.end_fill()

class Stem:
    def draw(self, t):
        t.color("green")
        h = t.heading()
        t.setheading(h - 90)
        t.forward(100)
        t.setheading(h)

class Leaf:
    def draw(self, t):
        t.color("green")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

class Flower(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.p = Petal()
        self.s = Stem()
        self.l = Leaf()

    def _render(self):
        self.s.draw(self.t)
        self.t.penup()
        self.t.goto(self.x, self.y - 50)
        self.t.pendown()
        self.l.draw(self.t)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for _ in range(6):
            self.p.draw(self.t, self.color)
            self.t.right(60)

n = int(input("Скільки квіток? "))
bouquet = [Flower(-200 + i * 150, 0, "red") for i in range(n)]

for _ in range(20):
    for f in bouquet:
        f.move(5, 5)
        f.rotate(15)

turtle.done()