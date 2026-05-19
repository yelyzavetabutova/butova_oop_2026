from Visitor import StudentVisitor

class ScholarshipVisitor(StudentVisitor):
    def __init__(self, amount):
        self.amount = amount

    def _add_money(self, student):
        if not student.is_expelled:
            student.money += self.amount

    def visit_humanitarian(self, student): self._add_money(student)
    def visit_natural(self, student): self._add_money(student)
    def visit_mixed(self, student): self._add_money(student)