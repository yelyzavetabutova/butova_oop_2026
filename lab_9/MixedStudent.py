from Student import Student
from Visitor import StudentVisitor

class MixedStudent(Student):
    def accept(self, visitor: StudentVisitor):
        visitor.visit_mixed(self)