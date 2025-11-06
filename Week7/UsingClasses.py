from classes import Person, Student, Employee, Car, Book, BankAccount

Person_1 = Person("Alice", 30, "123 Main St","Female")
Person_2 = Person("Bob", 25, "456 Elm St","Male")  
Person_3 = Person("Charlie", 35, "789 Oak St", "Male")

Student_1 = Student("S001", "David", "Computer Science", 2)
Student_2 = Student("S002", "Eva", "Mathematics", 3)
Student_3 = Student("S003", "Frank", "Physics", 1)

Employee_1 = Employee("E001", "Grace", "Manager", 60000)
Employee_2 = Employee("E002", "Hannah", "Developer", 50000)
Employee_3 = Employee("E003", "Ian", "Designer", 45000)

book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925)
book_2 = Book("1984", "George Orwell", "Secker & Warburg", 1949)
book_3 = Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", 1960)

Car_1 = Car("Toyota", "Camry", 2020, "Blue")
Car_2 = Car("Honda", "Civic", 2019, "Red")
Car_3 = Car("Ford", "Mustang", 2021, "Black")

BankAccount_1 = BankAccount("BA001", "Jack", 1500.75)
BankAccount_2 = BankAccount("BA002", "Kathy", 2500.00)
BankAccount_3 = BankAccount("BA003", "Liam", 3200.50)

with open("persons.txt", "w") as file:
    for person in [Person_1, Person_2, Person_3]:
        file.write(f"Name: {person.name}\nAge: {person.age}\nAddress: {person.address}\nGender: {person.gender}\n\n")
with open("students.txt", "w") as file:
    for student in [Student_1, Student_2, Student_3]:
        file.write(f"Student ID: {student.student_id}\nName: {student.name}\nCourse: {student.course}\nYear Level: {student.year_level}\n\n")
with open("employees.txt", "w") as file:
    for employee in [Employee_1, Employee_2, Employee_3]:
        file.write(f"Employee ID: {employee.employee_id}\nName: {employee.name}\nPosition: {employee.position}\nSalary: {employee.salary}\n\n")
with open("cars.txt", "w") as file:
    for car in [Car_1, Car_2, Car_3]:
        file.write(f"Make: {car.make}\nModel: {car.model}\nYear: {car.year}\nColor: {car.color}\n\n")
with open("books.txt", "w") as file:
    for book in [book_1, book_2, book_3]:
        file.write(f"Title: {book.title}\nAuthor: {book.author}\nPublisher: {book.publisher}\nYear Published: {book.year_published}\n\n")