class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50

student1 = Student("Kamil Noga", [60, 70, 80, 90])
student2 = Student("Kamil Slimak", [20, 30, 40, 25])

wynik1 = student1.is_passed()
wynik2 = student2.is_passed()

print(f"{student1.name} - Zdane: {wynik1}")
print(f"{student2.name} - Zdane: {wynik2}")
