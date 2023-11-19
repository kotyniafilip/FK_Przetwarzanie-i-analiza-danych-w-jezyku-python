class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}\nZip Code: {self.zip_code}\nOpen Hours: {self.open_hours}\nPhone: {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nAddress: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublication Date: {self.publication_date}\nNumber of Pages: {self.number_of_pages}\nLibrary: {self.library}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"{book.author_name} {book.author_surname}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student}\nOrder Date: {self.order_date}\nBooks:\n{book_list}"

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