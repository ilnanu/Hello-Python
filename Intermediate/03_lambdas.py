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
#2. Crea una lambda que calcule el cuadrado de un número.
#3. Crea una lambda que devuelva el mayor de dos números.
#4. Crea una lambda que sume 10 a un número dado.
#5. Crea una lambda que devuelva el último carácter de una cadena.
#6. Crea una lambda que indique si una palabra tiene más de 6 letras.
#7. Crea una lambda que convierta una cadena a minúsculas.
#8. Crea una lambda que devuelva True si un número es positivo.
#9. Crea una lambda que devuelva "Cadena vacía" si el string está vacío.
#10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.