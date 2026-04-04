import turtle
import random

class Figure:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
        self.visible = False
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.dx = random.choice([-3, -2, 2, 3])
        self.dy = random.choice([-3, -2, 2, 3])

    def draw(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self._render()
        self.visible = True

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if abs(self.x) > 300: self.dx *= -1
        if abs(self.y) > 250: self.dy *= -1

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
        t.setheading(270)
        t.forward(100)


class Leaf:
    def draw(self, t):
        t.color("green")
        t.begin_fill()
        t.circle(10)
        t.end_fill()


# --- Квітка (твоя логіка формування) ---
class Flower(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.p, self.s, self.l = Petal(), Stem(), Leaf()

    def _render(self):
        # ТВОЄ ФОРМУВАННЯ КВІТКИ
        self.s.draw(self.t)
        self.t.penup()
        self.t.goto(self.x, self.y - 50)
        self.t.pendown()
        self.l.draw(self.t)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.setheading(0)
        self.t.pendown()
        for _ in range(6):
            self.p.draw(self.t, self.color)
            self.t.right(60)


# --- Налаштування екрану ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.tracer(0)

# Запитуємо кількість у користувача
n_input = screen.numinput("Квіти", "Скільки квіток запустити?", 3)
n = int(n_input)

# Список кольорів для різноманітності
colors = ["red", "orange", "blue", "purple", "pink", "gold"]

# Створюємо список об'єктів (букет) через звичайний цикл for
bouquet = []
for i in range(n):
    vipadkoviy_kolir = random.choice(colors)
    nova_kvitka = Flower(random.randint(-200, 200), random.randint(-100, 100), vipadkoviy_kolir)
    bouquet.append(nova_kvitka)

# --- Головний цикл руху (спрощений) ---
while True:
    for kvitka in bouquet:
        kvitka.move()  # Викликаємо метод руху, який ми написали в класі

    screen.update()  # Оновлюємо екран, щоб побачити зміни