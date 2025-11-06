class Person:
    def __init__(self,name,age,address,gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
    
class Student:
    def __init__(self,student_id,name,course,year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

class Book:
    """
    Represents a book with its title, author, publisher, and year published.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        publisher (str): The publisher of the book.
        year_published (int): The year the book was published.
    """
    def __init__(self,title,author,publisher,year_published):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year_published = year_published

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance  