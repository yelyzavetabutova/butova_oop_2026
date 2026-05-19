from Visitor import StudentVisitor

class NaturalTeacherVisitor(StudentVisitor):
    def __init__(self, credits_to_give):
        self.credits = credits_to_give

    def visit_humanitarian(self, student):
        pass

    def visit_natural(self, student):
        student.earned_credits += self.credits

    def visit_mixed(self, student):
        student.earned_credits += self.credits