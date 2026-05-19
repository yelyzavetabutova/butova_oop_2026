from Visitor import StudentVisitor

class CostVisitor(StudentVisitor):
    def __init__(self, amount):
        self.amount = amount

    def _pay(self, student):
        if student.is_expelled:
            return
        if student.money >= self.amount:
            student.money -= self.amount
        else:
            student.is_expelled = True

    def visit_humanitarian(self, student): self._pay(student)
    def visit_natural(self, student): self._pay(student)
    def visit_mixed(self, student): self._pay(student)