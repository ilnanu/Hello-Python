# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
my_number = int(input("Introduce un número: "))
if my_number > 0:
    print("El número es positivo.")
elif my_number < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
my_edad = int(input("Introduce tu edad: "))
if my_edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
my_cadena = input("Introduce una cadena de texto: ")
if len(my_cadena) == 0:
    print("La cadena de texto está vacía.")
else:
    print("La cadena de texto no está vacía.")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
my_number1 = int(input("Introduce un número: "))
my_number2 = int(input("Introduce otro número: "))
if my_number1 > my_number2:
    print("El primer número es mayor que el segundo.")
elif my_number1 < my_number2:
    print("El segundo número es mayor que el primero.")
else:
    print("Los números son iguales.")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
my_number = int(input("Introduce un número: "))
if my_number % 3 == 0 and my_number % 5 == 0:
    print("El número es divisible por 3 y por 5.")
else:
    print("El número no es divisible por 3 y por 5.")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
my_number = int(input("Introduce un número: "))
if my_number % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
my_edad = int(input("Introduce tu edad: "))
if my_edad >= 18:
    print("Puedes votar.")
elif my_edad == 16 or my_edad == 17:
    print("Puedes votar con permiso especial.")
else:
    print("No puedes votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
my_user = input("Introduce un usuario: ")
my_password = input("Introduce una contraseña: ")
if my_user == "admin" and my_password == "1234":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
my_number = int(input("Introduce un número: "))
if my_number >= 10 and my_number <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está entre 10 y 20.")


# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
my_color = input("Introduce un color (rojo, amarillo, verde): ")
if my_color == "rojo":
    print("Detente.")
elif my_color == "amarillo":
    print("Estate alerta.")
elif my_color == "verde":
    print("Avanza.")
else:
    print("Color no válido.")
