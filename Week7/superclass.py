class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

class Dog(Animal):
    def __init__(self, name, species, age, breed):
        super().__init__(name, species, age)
        self.__breed = breed

    def __str__(self):
        return super().__str__() + f" It is a {self.__breed}."

class Cat(Animal):
    def __init__(self, name, species, age, color):
        super().__init__(name, species, age)
        self.__color = color

    def __str__(self):
        return super().__str__() + f" It is a {self.__color}."
    
#usage:
my_dog = Dog("Buddy", "Dog", 3, "Golden Retriever")
my_cat = Cat("Whiskers", "Cat", 2, "Tabby")

print(my_dog)  # Outputs: Buddy is a 3-year-old Dog. It is a Golden Retriever.
print(my_cat)  # Outputs: Whiskers is a 2-year-old Cat. It is a Tabby.

class Vehicle:
    def __init__(self, color, model, make_year, fuel_type):
        self.color = color
        self.model = model
        self.make_year = make_year
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.color} {self.model}, Year: {self.make_year}, Fuel Type: {self.fuel_type}"


class Car(Vehicle):
    def __init__(self, color, model, make_year, fuel_type, number_of_doors):
        super().__init__(color, model, make_year, fuel_type)
        self.__number_of_doors = number_of_doors

    def __str__(self):
        return super().__str__() + f", Number of Doors: {self.__number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, color, model, make_year, fuel_type, number_of_wheels):
        super().__init__(color, model, make_year, fuel_type)
        self.__number_of_wheels = number_of_wheels

    def __str__(self):
        return super().__str__() + f", Number of Wheels: {self.__number_of_wheels}"



#Usage
my_car = Car("Red", "Toyota", 2021, "Petrol", 4)
my_motorcycle = Motorcycle("Blue", "Yamaha", 2020, "Petrol", 2)

print(my_car)           # Outputs: Red Toyota, Year: 2021, Fuel Type: Petrol, Number of Doors: 4
print(my_motorcycle)    # Outputs: Blue Yamaha, Year: 2020, Fuel Type: Petrol, Number of Wheels: 2
