# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Sonido genérico")
print("Ejercicio 1:")
animal = Animal("Perro")
print(animal.species)
animal.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        if self.species == "Perro":
            print("Guau guau")
        elif self.species == "Gato":
            print("Miau miau")
        else:
            print("Sonido genérico")
print("Ejercicio 2:")
animal = Animal("Perro")
print(animal.species)
animal.make_sound()
animal = Animal("Gato")
print(animal.species)
animal.make_sound()
animal = Animal("Pájaro")
print(animal.species)
animal.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
print("Ejercicio 3:")
car = Car("Ford", "Focus")
print(car.brand)
print(car.model)
print(car._speed)

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

    def accelerate(self):
        self._speed += 10

    def brake(self):
        self._speed -= 10
        if self._speed < 0:
            self._speed = 0
print("Ejercicio 4:")
car = Car("Ford", "Focus")
print(car._speed)
car.accelerate()
print(car._speed)
car.brake()
print(car._speed)
car.brake()
print(car._speed)

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self._author = author

    def get_author(self):
        return self._author

    def set_title(self, title):
        self.title = title      
print("Ejercicio 5:")
book = Book("El Quijote", "Miguel de Cervantes")
print(book.title)
print(book.get_author())
book.set_title("Don Quijote")
print(book.title)

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
print("Ejercicio 6:")
student = Student("Brais", "Moure", [7, 8, 9])
print(student.name)
print(student.surname)
print(student.grades)
print(student.calculate_average())

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("No hay suficiente saldo.")       
print("Ejercicio 7:")
account = BankAccount("Brais", 1000)
print(account.owner)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(200)
print(account.balance)
account.withdraw(2000)
print(account.balance)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5       
print("Ejercicio 8:")
point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.calculate_distance(point2))

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_payment(self):
        return self.hourly_wage * self.hours_worked     
print("Ejercicio 9:")
employee = Employee("Brais", 10, 40)
print(employee.name)
print(employee.hourly_wage)
print(employee.hours_worked)
print(employee.calculate_payment())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def show_inventory(self):
        for product in self.inventory:
            print(product)      
print("Ejercicio 10:")
store = Store()
store.add_product("Leche")
store.add_product("Pan")
store.add_product("Huevos")
store.show_inventory()
