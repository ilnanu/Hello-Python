# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)

#EJERCICIOS

#1. Genera una lista utilizando comprensión con los números del 0 al 10.
my_list = [i for i in range(11)]
print(my_list)

#2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.
my_list = [i * i for i in range(1, 11)]
print(my_list)  

#3. Genera una lista utilizando comprensión con los números pares del 0 al 20.
my_list = [i for i in range(21) if i % 2 == 0]
print(my_list)

#4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.
my_list = [temp * 9 / 5 + 32 for temp in [0, 10, 20, 30, 40]]
print(my_list)

#5. Crea una lista utilizando comprensión con los caracteres de una cadena.
my_string = "Hola"
my_list = [char for char in my_string]
print(my_list)

#6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.
my_list = [word for word in ["Hola", "mundo", "Python", "es", "genial"] if len(word) > 4]
print(my_list)

#7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.
def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
print(my_list)

#8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.
my_list = [num > 10 for num in [5, 10, 15, 20, 25]]
print(my_list)

#9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.
my_list = [num * 3 for num in [1, 2, 3, 4, 5] if num % 2 != 0]
print(my_list)

#10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.
my_list = [[i + j * 3 for i in range(1, 4)] for j in range(3)]
print(my_list)
