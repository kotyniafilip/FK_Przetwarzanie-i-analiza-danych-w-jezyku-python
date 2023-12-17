from typing import List

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50
