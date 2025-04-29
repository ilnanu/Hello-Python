# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###

def sum_two_values(
    first_value, second_value): return first_value + second_value


print(sum_two_values(2, 4))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3


print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))

# Ejercicios Lambdas

#1. Crea una lambda que sume dos números.
def sum_two_numbers(a, b): return a + b
print(sum_two_numbers(3, 5))

#2. Crea una lambda que calcule el cuadrado de un número.
def square_number(x): return x * x
print(square_number(4))

#3. Crea una lambda que devuelva el mayor de dos números.
def max_of_two(a, b): return a if a > b else b
print(max_of_two(10, 5))

#4. Crea una lambda que sume 10 a un número dado.
def add_ten(x): return x + 10
print(add_ten(5))

#5. Crea una lambda que devuelva el último carácter de una cadena.
def last_character(string): return string[-1] if string else None
print(last_character("Python"))

#6. Crea una lambda que indique si una palabra tiene más de 6 letras.
def has_more_than_six_letters(word): return len(word) > 6
print(has_more_than_six_letters("Pythonista"))

#7. Crea una lambda que convierta una cadena a minúsculas.
def to_lowercase(string): return string.lower()
print(to_lowercase("PYTHON"))

#8. Crea una lambda que devuelva True si un número es positivo.
def is_positive(number): return number > 0
print(is_positive(5))

#9. Crea una lambda que devuelva "Cadena vacía" si el string está vacío.
def empty_string(string): return "Cadena vacía" if not string else string
print(empty_string(""))
print(empty_string("Python"))   

#10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.
def final_price(price): return price * 1.21
print(final_price(100))
