# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))

#Ejercicios Funciones de orden superior

#1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.
def apply_function(func, number):
    return func(number) 
def square(x):
    return x * x
print(apply_function(square, 5)) #25


#2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.
def apply_function_to_sum(func, a, b):
    return func(a + b)
def double(x):
    return x * 2
print(apply_function_to_sum(double, 2, 3)) #10

#3. Crea una función que devuelva otra función que sume un número fijo.
def add_fixed_value(fixed_value):
    def add(value):
        return value + fixed_value
    return add
add_five = add_fixed_value(5)
print(add_five(10)) #15

#4. Usa map() con lambda para multiplicar cada número de una lista por 10.
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 10, numbers))) # [10, 20, 30, 40, 50]

#5. Usa filter() con lambda para quedarte solo con los números pares.
numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, numbers))) # [2, 4, 6]

#6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, numbers)) #15

#7. Escribe una función que devuelva una función que reciba un nombre y devuelva "Hola, ".
# seguido del nombre.
def greet(greeting):
    def say_hello(name):
        return f"{greeting}, {name}"
    return say_hello    
def hello(name):
    return greet("Hola")(name)
print(hello("Juan")) #Hola, Juan

#8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.
def count_elements(lst, func):
    return len(list(filter(func, lst)))
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
print(count_elements(numbers, is_even)) #3

#9. Crea una función que reciba dos funciones y un número, y las aplique en orden.
def apply_functions_in_order(func1, func2, number):
    return func2(func1(number))
def add_one(x):
    return x + 1
def multiply_by_two(x):
    return x * 2
print(apply_functions_in_order(add_one, multiply_by_two, 5)) #12

#10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).
def apply_function_with_loop(lst, func):
    result = []
    for item in lst:
        result.append(func(item))
    return result
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
print(apply_function_with_loop(numbers, square)) # [1, 4, 9, 16, 25]
#
#11. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).
def apply_function_with_loop(lst, func):
    result = []
    for item in lst:
        result.append(func(item))
    return result
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
print(apply_function_with_loop(numbers, square)) # [1, 4, 9, 16, 25]
