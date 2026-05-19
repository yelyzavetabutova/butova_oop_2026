from Student import Student
from Visitor import StudentVisitor

class HumanitarianStudent(Student):
    def accept(self, visitor: StudentVisitor):
        visitor.visit_humanitarian(self)