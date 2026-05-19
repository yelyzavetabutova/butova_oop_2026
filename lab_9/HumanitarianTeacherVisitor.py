from Visitor import StudentVisitor

class HumanitarianTeacherVisitor(StudentVisitor):
    def __init__(self, credits_to_give):
        self.credits = credits_to_give

    def visit_humanitarian(self, student):
        student.earned_credits += self.credits

    def visit_natural(self, student):
        pass

    def visit_mixed(self, student):
        student.earned_credits += self.credits