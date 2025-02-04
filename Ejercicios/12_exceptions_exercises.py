# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
def divide_numbers():
    try:
        number1 = int(input("Introduce un número: "))
        number2 = int(input("Introduce otro número: "))
        result = number1 / number2
        print(f"El resultado de la división es {result}")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
divide_numbers()

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.
def convert_to_integer(text):
    try:
        number = int(text)
        print(f"El número es {number}")
    except ValueError:
        print("No se pudo convertir la cadena en un número entero.")
convert_to_integer("Hola")

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
read_file("file.txt")

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def operations(number1, number2):
    try:
        print(f"Suma: {number1 + number2}")
        print(f"Resta: {number1 - number2}")
        print(f"División: {number1 / number2}")
        print(f"Multiplicación: {number1 * number2}")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else:
        print("Operaciones realizadas con éxito.")
    finally:
        print("Operaciones finalizadas.")
operations(10, 0)

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def get_age():
    try:
        age = int(input("Introduce tu edad: "))
        if age < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        print(f"Tu edad es {age}")
    except ValueError as e:
        print(e)
get_age()

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.
def get_element(my_list, index):
    try:
        print(my_list[index])
    except IndexError:
        print("El índice está fuera de rango.")
get_element([1, 2, 3], 3)

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def multiple_exceptions():
    try:
        number = int(input("Introduce un número: "))
        result = 10 / number
        print(result)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except ValueError:
        print("La entrada no es un número válido.")
    except TypeError:
        print("Error de tipo.")
multiple_exceptions()

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
def transaction(balance, amount):
    class InsufficientFundsError(Exception):
        pass
    try:
        if amount > balance:
            raise InsufficientFundsError("Saldo insuficiente.")
        balance -= amount
        print(f"Transacción exitosa. Saldo restante: {balance}")
    except InsufficientFundsError as e:
        print(e)
transaction(100, 200)

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def convert_to_integers(my_list):
    try:
        integers = [int(value) for value in my_list]
        print(integers)
    except ValueError:
        print("Error al convertir las cadenas en enteros.")
convert_to_integers(["1", "2", "3", "a"])

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.
def calculate_square_root(number):
    if number < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return number ** 0.5
try:
    print(calculate_square_root(-1))
except ValueError as e:
    print(e)    
