# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
import calculator

print(calculator.sum(2, 3))
print(calculator.subtract(5, 3))
print(calculator.multiply(2, 3))
print(calculator.divide(6, 3))


# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
import converter

print(converter.celsius_to_fahrenheit(0))
print(converter.celsius_to_fahrenheit(100))


# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
import lista_nombres

lista_nombres.print_students()

# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.

import geometry

print(geometry.circle_area(5))
print(geometry.square_area(5))


# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
import operaciones

print(operaciones.sum(1, 2, 3, 4, 5))


# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".

import cars

car = cars.Car("Toyota", "Corolla", 2020)
print(car.brand)
print(car.model)
print(car.year)

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

import archivos as ficheros

ficheros.write_file("data.txt", "Hello, world!")
print(ficheros.read_file("data.txt"))


# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
import statistics

numbers = [1, 2, 3, 4, 5]
print(statistics.mean(numbers))
print(statistics.median(numbers))

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

import operaciones

text = "Hello, world! Hello, Python!"
print(operaciones.count_words(text, "Hello"))

# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
import dates    

print(dates.get_current_date())
print(dates.get_date_diff("2021-01-01", "2021-12-31"))
