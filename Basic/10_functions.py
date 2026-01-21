# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición


def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

# Assigning a function to a variable in Python:


def add():
    print("We assigned function to variable")


# Assign function to variable
sum = add
# calling function
sum()


# Pass function as a parameter to another function in Python
def display(x):
    print("This is display function")


def message():
    print("This is message function")


# calling function
display(message())

# Define one function inside another function in Python:


def first():
    print("This is outer function")

    def second():
        print("this is inner function")

    second()


# calling outer function
first()


# The function can return another function in Python:


def first():
    def second():
        print("This function is return type to outer function")

    return second


x = first()
x()


# Factorial using the recursive function in python (Demo33.py)
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


x = factorial(4)
print("Factorial of 4 is: ", x)

# Lambda Function in Python (Demo35.py)
s = lambda a: a * a
x = s(4)
print(x)

# Lambda Function in Python (Demo36.py)
add = lambda a, b: a + b
x = add(4, 5)
print(x)

# Filter Function in python (Demo37.py)
items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x: x > 1000, items_cost)
x = list(gt_thousand)
print("Eligible for discount: ", x)

# Map Function in Python (Demo38.py)
without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)

# Reduce Function (Demo39.py)
from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)

#Decorator
def add(a,b):
   res = a + b
   return res
print(add(20,30))
print(add(-10,5))

def decor(func):  #Here ‘func’ is the the argument/parameter which receives the function 
    def inner_function(x,y):
        if x<0:
            x = 0
        if y<0:
            y = 0
        return func(x,y)
    return inner_function  #Decor returns the func passed to it.

add = decor(add)
print(add(20,30))
print(add(-10,5))

# @ symbol in python
def decor(func):
   def inner_function(x,y):
       if x<0:
           x = 0
       if y<0:
           y = 0
       return func(x,y)
   return inner_function 

@decor
def sub(a,b):
   res = a - b
   return res

print(sub(30,20))
print(sub(10,-5))

#Generators in Python
def m():
   yield 'Mahesh'
   yield 'Suresh'

g = m()
print(g)
print(type(g))
for y in g:
   print(y)

def m(x, y):
   while x<=y:
       yield x
       x+=1

g = m(5, 10)
for y in g:
   print(y)

#next function in Python
def m():
   yield 'Mahesh'
   yield 'Suresh'
g = m()

print(type(g))
print(next(g))
print(next(g))

#dir() function in Python
x=10
y=20
def f1():
   print("Hello")
print(dir())