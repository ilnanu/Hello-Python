# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición


class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)


# DotNetTutorials Examples
class Employee:
    def display(
        self,
    ):  # self is a default variable that refers to a current class object or the current instance(object) of a class. Como this en .Net
        print("Hello my name is Shiksha")


emp_obj = Employee()
emp_obj.display()


class Employee:
    def __init__(
        self,
    ):  # constructor is a method with the name ‘__init__’. The methods first parameter should be ‘self’ (referring to the current object). Optional
        print("constructor")


emp = Employee()
emp.__init__()
print(dir(Employee))


# constructor con parametros
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("Hello my id is :", self.id)
        print("My name is :", self.name)


e1 = Employee(1, "Nithin")
e1.display()
e2 = Employee(2, "Arjun")
e2.display()


# Instance Variables
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student("Nitya", 1)
s2 = Student("Anushka", 2)
print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)


class Employee:
    def __init__(self):
        self.eno = 1
        self.ename = "Nithya"
        self.esal = 100


e = Employee()

print("Employee number: ", e.eno)
print("Employee name: ", e.ename)
print("Employee salary: ", e.esal)
print(e.__dict__)


class Student:
    def m1(self):
        self.a = 11
        self.b = 21
        self.c = 34
        print(self.a)
        print(self.b)
        print(self.c)


s = Student()
s.m1()
print(s.__dict__)


class Test:
    def __init__(self):
        print("This is constructor")

    def m1(self):
        print("This is instance method")


t = Test()
t.m1()
t.a = 10
t.b = 20
t.c = 55
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)


# Static Variables
class Student:
    college_name = "GITAM"  # static

    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student("Nithya", 1)
s2 = Student("Anushka", 2)

print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name n : ", Student.college_name)

print("\n")
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)
print("College name : ", Student.college_name)


class Student:
    college_name = "GITAM"

    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student("Nithya", 1)
s2 = Student("Anushka", 2)

print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name n : ", s1.college_name)

print("\n")
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)
print("College name : ", s1.college_name)

# Declaring static variables


class Demo:
    a = 20

    def m(self):
        print("this is method")


print(Demo.__dict__)


class Demo:
    def __init__(self):
        Demo.b = 20


d = Demo()
print(Demo.__dict__)


class Demo:
    def m1(self):
        Demo.b = 20


obj = Demo()
obj.m1()
print(Demo.__dict__)


# class method


class Demo:
    @classmethod
    def m2(cls):
        Demo.b = 30


obj = Demo()
obj.m2()
print(Demo.__dict__)


class Demo:
    @classmethod
    def m2(cls):
        cls.b = 30


obj = Demo()
obj.m2()
print(Demo.__dict__)


class Demo:
    @staticmethod
    def m3():
        Demo.z = 10


Demo.m3()
print(Demo.__dict__)


class Demo:
    a = 10

    def __init__(self):
        print(self.a)
        print(Demo.a)


d = Demo()


class Demo:
    a = 10

    def m1(self):
        print(self.a)
        print(Demo.a)


obj = Demo()
obj.m1()


class Demo:
    a = 10

    @classmethod
    def m1(cls):
        print(cls.a)
        print(Demo.a)


obj = Demo()
obj.m1()


class Demo:
    a = 10

    @staticmethod
    def m1():
        print(Demo.a)


obj = Demo()
obj.m1()

# Local Variables


class Demo:
    def m(self):
        a = 10  # Local Variable
        print(a)


d = Demo()
d.m()


class Demo:
    def m(self):
        a = 10  # Local Variable
        print(a)

    def n(self):
        print(a)  #'a' is local variable of m()


d = Demo()

# Types of Class Methods in Python


##Instance Methods
class Demo:
    def __init__(self, a):
        self.a = a

    def m(self):
        print(self.a)


d = Demo(10)
d.m()


# Setter and Getter methods
class Customer:
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id


c = Customer()
c.set_name("Balayya")
c.set_id(1)

print(c.name)


class Customer:
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


c = Customer()
c.set_name("Balayya")
c.set_id(1)

print("My name is: ", c.get_name())
print("My id is: ", c.get_id())


##Class Methods in Python
class Pizza:
    radius = 200

    @classmethod
    def get_radius(cls):
        return cls.radius


print(Pizza.get_radius())


##Static Methods
class Demo:
    @staticmethod
    def sum(x, y):
        print(x + y)

    @staticmethod
    def multiply(x, y):
        print(x * y)


Demo.sum(2, 3)
Demo.multiply(2, 4)


# Nested Classes
class A:
    def __init__(self):
        print("outer class object creation")

    class B:
        def __init__(self):
            print("inner class object creation")

        def m1(self):
            print("inner class method")


a = A()
b = a.B()
b.m1()

# Garbage Collection
import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())


# Herencia
class One:
    def m1(self):
        print("Parent class m1 method")


class Two(One):
    def m2(self):
        print("Child class m2 method")


c = Two()
c.m1()
c.m2()


##Single Inheritance
class A:
    def m1(self):
        print("A class m1 Method")


class B(A):
    def m2(self):
        print("Child B is derived from A class: m2 Method")


obj = B()
obj.m1()
obj.m2()


##Multilevel inheritance
class A:
    def m1(self):
        print("Parent class A: m1 Method")


class B(A):
    def m2(self):
        print("Child class B derived from A: m2 Method")


class C(B):
    def m3(self):
        print("Child class C derived from B: m3 Method")


obj = C()
obj.m1()
obj.m2()
obj.m3()


class P1:
    def m1(self):
        print("Parent1 Method")


class P2:
    def m2(self):
        print("Parent2 Method")


class C(P1, P2):
    def m3(self):
        print("Child Method")


c = C()
c.m1()
c.m2()
c.m3()


class P1:
    def m1(self):
        print("Parent1 Method")


class P2:
    def m1(self):
        print("Parent2 Method")


class C(P1, P2):
    def m2(self):
        print("Child Method")


c = C()
c.m2()


class P1:
    def m1(self):
        print("Parent1 Method")


class P2:
    def m1(self):
        print("Parent2 Method")


class C(P1, P2):
    def m2(self):
        print("Child Method")


c = C()
c.m2()
c.m1()


class P1:
    def m1(self):
        print("Parent1 Method")


class P2:
    def m1(self):
        print("Parent2 Method")


class C(P2, P1):
    def m2(self):
        print("Child Method")


c = C()
c.m2()
c.m1()

# CONSTRUCTORS in INHERITANCE


class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def m1():
        print("Child Class B: m1 method from B")


b = B()


class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def __init__(self):
        print("Child class B constructor")


b = B()


class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def __init__(self):
        print("Child class B constructor")
        super().__init__()


b = B()


# Method Resolution Order (MRO)


class A:
    def m1(self):
        print("m1 from A")


class B(A):
    def m1(self):
        print("m1 from B")


class C(A):
    def m1(self):
        print("m1 from C")


class D(B, C):
    def m1(self):
        print("m1 from D")


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())


class A:
    def m1(self):
        print("m1 from A")


class B(A):
    def m1(self):
        print("m1 from B")


class C(A):
    def m1(self):
        print("m1 from C")


class D(B, C):
    def m1(self):
        print("m1 from D")


c = C()
c.m1()
print(C.mro())


class A:
    def m1(self):
        print("m1 from A")


class B(A):
    def m1(self):
        print("m1 from B")


class C(A):
    def m2(self):
        print("m2 from C")


class D(B, C):
    def m1(self):
        print("m1 from D")


c = C()
c.m1()
print(C.mro())


class A:
    def m1(self):
        print("m1 from A")


class B(A):
    def m1(self):
        print("m1 from B")


class C(A):
    def m1(self):
        print("m1 from C")


class D(B, C):
    def m1(self):
        print("m1 from D")


d = D()
d.m1()
print(D.mro())


class A:
    def m1(self):
        print("m1 from A")


class B(A):
    def m2(self):
        print("m1 from B")


class C(A):
    def m1(self):
        print("m1 from C")


class D(B, C):
    def m3(self):
        print("m3 from D")


d = D()
d.m1()
print(D.mro())


class A:
    def m1(self):
        print("m1 from A")


class B:
    def m1(self):
        print("m1 from B")


class C:
    def m1(self):
        print("m1 from C")


class X(A, B):
    def m1(self):
        print("m1 from C")


class Y(B, C):
    def m1(self):
        print("m1 from A")


class P(X, Y, C):
    def m1(self):
        print("m1 from P")


print(A.mro())  # AO
print(X.mro())  # XABO
print(Y.mro())  # YBCO
print(P.mro())  # PXAYBCO


# Super Function in Python
class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def __init__(self):
        print("Child class B constructor")
        super().__init__()


b = B()


class A:
    def m1(self):
        print("Super class A: m1 method")


class B(A):
    def m1(self):
        print("Child class B: m1 method")
        super().m1()


b = B()
b.m1()


class A:
    x = 10

    def m1(self):
        print("Super class A: m1 method")


class B(A):
    x = 20

    def m1(self):
        print("Child class x variable", self.x)
        print("Super class x variable", super().x)


b = B()
b.m1()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, empno, address):
        super().__init__(name, age)
        self.empno = empno
        self.address = address

    def display(self):
        super().display()
        print("Emp No:", self.empno)
        print("Address:", self.address)


e1 = Employee("Neethu", 16, 111, "Delhi")
e1.display()


class A:
    def m1(self):
        print("m1() method from A class")


class B(A):
    def m1(self):
        print("m1() method from B class")


class C(B):
    def m1(self):
        print("m1() method from C class")


class D(C):
    def m1(self):
        print("m1() method from D class")


class E(D):
    def m1(self):
        A.m1(self)


e = E()
e.m1()


class A:
    def m1(self):
        print("m1() method from A class")


class B(A):
    def m1(self):
        print("m1() method from B class")


class C(B):
    def m1(self):
        print("m1() method from C class")


class D(C):
    def m1(self):
        print("m1() method from D class")


class E(D):
    def m1(self):
        # A.m1(self)
        super(D, self).m1()


e = E()
e.m1()

"""
class P:
   def __init__(self):
       self.a=20
class C(P):
   def m1(self):
       print(super().a)

c=C()
c.m1()
"""


class P:
    def __init__(self):
        self.a = 20


class C(P):
    def m1(self):
        print(self.a)


c = C()
c.m1()


class P:
    a = 10

    def m1(self):
        print("m1 from Parent class")


class C(P):
    def m2(self):
        print(super().a)


c = C()
c.m2()


class P:
    def __init__(self):
        print("Parent class Constructor")

    def m1(self):
        print("m1() instance method from Parent class")

    @classmethod
    def m2(cls):
        print("m2() class method from Parent class")

    @staticmethod
    def m3():
        print("m3() static method from Parent class")


class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()


class P:
    def __init__(self):
        print("Parent class Constructor")

    def m1(self):
        print("m1() instance method from Parent class")

    @classmethod
    def m2(cls):
        print("m2() class method from Parent class")

    @staticmethod
    def m3():
        print("m3() static method from Parent class")


class C(P):
    def __init__(self):
        print("Child class constructor")

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()
c.m1()

"""
class P:
   def __init__(self):
       print('Parent Constructor')
   def m1(self):
       print('Parent instance method')
   @classmethod
   def m2(cls):
       print('Parent class method')
   @staticmethod
   def m3():
       print('Parent static method')
class C(P):
   @classmethod
   def m1(cls):
       super().__init__()
       super().m1()

C.m1()
"""


class P:
    def __init__(self):
        print("Parent Constructor")

    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent static method")


class C(P):
    @classmethod
    def m1(cls):
        super().m2()
        super().m3()


C.m1()


class P:
    def __init__(self):
        print("Parent Constructor")

    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent static method")


class C(P):
    @classmethod
    def m1(cls):
        super(C, cls).__init__(cls)
        super(C, cls).m1(cls)


C.m1()

# Polymorphism in Python


## Duck typing philosophy
class Duck:
    def talk(self):
        print("Quack.. Quack")


class Dog:
    def talk(self):
        print("Bow...Bow")


class Cat:
    def talk(self):
        print("Moew...Moew ")


def m(obj):
    obj.talk()


duck = Duck()
m(duck)

cat = Cat()
m(cat)

dog = Dog()
m(dog)

# Operator overloading
print(10 + 20)
print("Python" + "Programming")
print([1, 2, 3] + [4, 5, 6])

print(10 * 20)
print("Python" * 3)
print([1, 2, 3] * 3)


# Addition Operator (+)
class Book:
    def __init__(self, pages):
        self.pages = pages


b1 = Book(100)
b2 = Book(200)
print(type(b1))
print(type(b2))

print(type(b1.pages))
print(type(b2.pages))

print(b1.pages + b2.pages)
print((b1.pages).__add__(b2.pages))

"""
class Book:
   def __init__(self, pages):
       self.pages=pages

b1=Book(100)
b2=Book(200)

print(b1 + b2)
"""


# Magic Methods
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, others):
        return self.pages + others.pages


b1 = Book(100)
b2 = Book(200)

print(b1 + b2)

"""
class Student:
   def __init__(self, name, marks):
       self.name=name
       self.marks=marks


s1=Student("Samvida", 100)
s2=Student("Surya", 200)
print("s1>s2 =", s1>s2)
print("s1<s2 =", s1<s2)
print("s1<=s2 =", s1<=s2)
print("s1>=s2 =", s1>=s2)
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks <= other.marks


s1 = Student("Samvida", 100)
s2 = Student("Surya", 200)
print("s1>s2 =", s1 > s2)
print("s1<s2 =", s1 < s2)


# Method overloading
"""
class Demo:
   def m1(self):
       print('no-arg method')
   def m1(self, a):
       print('one-arg method')
   def m1(self, a, b):
       print('two-arg method')
      
d= Demo()
d.m1()
#d.m1(10)
#d.m1(10,20)


class Demo:
   def m1(self):
       print('no-arg method')
   def m1(self, a):
       print('one-arg method')
   def m1(self, a, b):
       print('two-arg method')

d= Demo()
#d.m1()
d.m1(10)
#d.m1(10,20)
"""


class Demo:
    def m1(self):
        print("no-arg method")

    def m1(self, a):
        print("one-arg method")

    def m1(self, a, b):
        print("two-arg method")


d = Demo()
# d.m1()
# d.m1(10)
d.m1(10, 20)


class Demo:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("The Sum of 3 Numbers:", a + b + c)
        elif a != None and b != None:
            print("The Sum of 2 Numbers:", a + b)
        else:
            print("Please provide 2 or 3 arguments")


d = Demo()
d.sum(10, 20, 30)
d.sum(10, 20)
d.sum(10)


class Demo:
    def sum(self, *a):
        total = 0
        for x in a:
            total = total + x
        print("The Sum:", total)


d = Demo()
d.sum(10, 20, 30)
d.sum(10, 20)
d.sum(10)

"""
class Demo:
   def __init__(self):
       print('No-Arg Constructor')
   def __init__(self, a):
       print('One-Arg constructor')
   def __init__(self, a, b):
       print('Two-Arg constructor')

d1=Demo()
#d1=Demo(10)
#d1=Demo(10,20)


class Demo:
   def __init__(self):
       print('No-Arg Constructor')
   def __init__(self, a):
       print('One-Arg constructor')
   def __init__(self, a, b):
       print('Two-Arg constructor')

#d1=Demo()
#d1=Demo(10)
d1=Demo(10,20)
"""


# Method Overriding in Python
class P:
    def properties_status(self):
        print("Money, Land, Gold")

    def to_marry(self):
        print("Anushka")


class C(P):
    def study_status(self):
        print("Studies done waiting for job")

    def to_marry(self):
        print("Megha")


c = C()
c.properties_status()
c.to_marry()
c.study_status()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)


e1 = Employee("Surabhi", 16, 872425, 26000)
e1.display()
e2 = Employee("Ranjith", 20, 872426, 36000)
e2.display()

# Abstract Classes in Python
from abc import *


class Demo1(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    def m3(self):
        print("Implemented method")


from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        "Implementation of abstract method"
        print("In sbi bank 5 rupees interest")


s = SBI()
s.bank_info()
s.interest()

from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass


# Sub class/ child class of abstract class
"""
class SBI(Bank):
    def balance(self):
        print("Balance is 100")


s = SBI()
s.bank_info()
s.balance()
"""

from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 100")


class Sub1(SBI):
    def interest(self):
        print("In sbi bank interest is 5 rupees")


s = Sub1()
s.bank_info()
s.balance()
s.interest()

from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass

    def offers(self):
        print("Providing offers")


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        print("In SBI bank 5 rupees interest")


s = SBI()
s.bank_info()
s.interest()

from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass

    def offers(self):
        print("Providing offers")


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        print("In SBI bank 5 rupees interest")


class HDFC(Bank):
    def interest(self):
        print("In HDFC 7 rupees interest")


s = SBI()
h = HDFC()
s.bank_info()
s.interest()
h.bank_info()
h.interest()

from abc import ABC, abstractmethod


class One(ABC):
    @abstractmethod
    def calculate(self, a):
        pass

    def m1(self):
        print("implemented method")


class Square(One):
    def calculate(self, a):
        print("square: ", (a * a))


"""
class Cube(One):
   def calculate(self, a):
       print("cube: ", (a*a*a))
s = Square()
c = Cube()
s.calculate(2)
c.calculate(2)
"""

from abc import *


class Demo:
    @abstractmethod
    def m(self):
        pass

    def n(self):
        print("Implemented method")


t = Demo()
t.m()
t.n()

# Interfaces in Python
from abc import ABC, abstractmethod
class Bank(ABC):
   @abstractmethod
   def balance_check(self):
       pass
   @abstractmethod
   def interest(self):
       pass

class SBI(Bank):
   def balance_check(self):
       print("Balance is 100 rupees")
   def interest(self):
       print("SBI interest is 5 rupees")


s = SBI()
s.balance_check()
s.interest()

from abc import *
class DBInterface(ABC):
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass

class Oracle(DBInterface):
   def connect(self):
       print('Connecting to Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Oracle Database...')

class Sybase(DBInterface):
   def connect(self):
       print('Connecting to Sybase Database...')
   def disconnect(self):
       print('Disconnecting to Sybase Database...')   

dbname=input('Enter Database Name either Oracle or Sybase:')
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()


class Student:
   def __init__(self, name, rollno):
       self.name=name
       self.rollno=rollno

   def __str__(self):
       return 'This is Student object with name {} and roll no {}'.format(self.name, self.rollno)
s1=Student('Ram',10)
s2=Student('Rahim' ,12)
print(s1)
print(s2)

