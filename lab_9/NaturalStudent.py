from Student import Student
from Visitor import StudentVisitor

class NaturalStudent(Student):
    def accept(self, visitor: StudentVisitor):
        visitor.visit_natural(self)