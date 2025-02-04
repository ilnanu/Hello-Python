# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="desconocido"):
    print(f"Hola, {name}")
personalized_greeting("Brais")

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(number1, number2):
    return number1 * number2
print(multiply(2, 3))

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(number):
    return number % 2 == 0
print(is_even(4))

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text):
    return text.upper() 
print(convert_to_uppercase("Hola"))

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers):
    return sum(numbers)
print(arbitrary_sum(1, 2, 3, 4, 5))

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    return f"Hola, {name} {surname}"
print(generate_full_greeting(name="Brais", surname="Moure"))

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponent):
    return base ** exponent
print(power(2, 3))

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(number1, number2, number3):
    return (number1 + number2 + number3) / 3
print(calculate_average(2, 4, 6))

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text):
    return len(text)
print(count_characters("Hola"))

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*messages):
    for message in messages:
        print(message.upper())
display_messages("Hola", "Adiós", "Buenos días")
