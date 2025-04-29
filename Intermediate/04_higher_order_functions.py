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

#2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.
#3. Crea una función que devuelva otra función que sume un número fijo.
#4. Usa map() con lambda para multiplicar cada número de una lista por 10.
#5. Usa filter() con lambda para quedarte solo con los números pares.
#6. Usa reduce() con lambda para obtener la suma total de una lista.
#7. Escribe una función que devuelva una función que reciba un nombre y devuelva "Hola, ".
#8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.
#9. Crea una función que reciba dos funciones y un número, y las aplique en orden.
#10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).