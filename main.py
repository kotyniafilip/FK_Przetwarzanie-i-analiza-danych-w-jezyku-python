from classes.Student import Student
from classes.Library import Library
from classes.Book import Book
from classes.Employee import Employee
from classes.Order import Order
from classes.House import House
from classes.Flat import Flat

library1 = Library("Jaworzno", "Grunwaldzka 20", "43600", "9:00 - 19:00", "123-456-789")
library2 = Library("Katowice", "Kwiatowa 10", "45200", "8:00 - 16:00", "123-456-789")

book1 = Book(library1, "11-11-2018", "Wojcierz", "Chmielarz", 350)
book2 = Book(library1, "01-01-2019", "Adam", "Rybak", 280)
book3 = Book(library1, "02-03-2015", "Kamil", "Noga", 410)
book4 = Book(library2, "15-07-2020", "Marta", "Sum", 210)
book5 = Book(library2, "27-05-2019", "Anna", "Górka", 480)

employee1 = Employee("Kamil", "Nowak", "2022-01-15", "1990-05-20", "Jaworzno", "Grunwaldzka 202", "43600", "111-222-333")
employee2 = Employee("Adam", "Kowalski", "2021-08-10", "1985-12-03", "Katowice", "Kwiatowa 2", "45600", "444-555-666")
employee3 = Employee("Galvin", "Klain", "2020-05-03", "1982-09-17", "Katowice", "Graniczna 12", "45600", "777-888-999")

student1 = "Anna Nowak"
student2 = "Kamil Tumulec"
student3 = "Adam Noga"

order1 = Order(employee1, student1, [book1, book2, book3], "2023-11-12")
order2 = Order(employee2, student2, [book4, book5], "2023-11-13")

print(order1)
print()
print(order2)

house = House(area=200, rooms=5, price=500000, address="Grunwaldzka 40", plot=10)
flat = Flat(area=70, rooms=3, price=100000, address="Jaśminowa 50", floor=7)

print(house)
print(flat)


