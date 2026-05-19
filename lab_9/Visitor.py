from abc import ABC, abstractmethod

class StudentVisitor(ABC):
    @abstractmethod
    def visit_humanitarian(self, student):
        pass

    @abstractmethod
    def visit_natural(self, student):
        pass

    @abstractmethod
    def visit_mixed(self, student):
        pass