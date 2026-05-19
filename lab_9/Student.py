from abc import ABC, abstractmethod
from Visitor import StudentVisitor

class Student(ABC):
    def __init__(self, required_credits, initial_money):
        self.required_credits = required_credits
        self.money = initial_money
        self.earned_credits = 0
        self.is_expelled = False

    @abstractmethod
    def accept(self, visitor: StudentVisitor):
        pass

    @property
    def has_graduated(self):
        return not self.is_expelled and self.earned_credits >= self.required_credits