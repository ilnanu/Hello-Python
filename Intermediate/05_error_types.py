# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=12721

### Error Types ###

# SyntaxError
# print "¡Hola comunidad!" # Descomentar para Error
from math import pi
import math
print("¡Hola comunidad!")

# NameError
language = "Spanish"  # Comentar para Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # Descomentar para Error
print(pi)

# ValueError
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)

#Ejercicios Tipos de error
#1. Genera un SyntaxError al imprimir una cadena sin paréntesis.
#from math import pi
#print "¡Hola comunidad!" # Descomentar para Error

#2. Genera un NameError intentando usar una variable no definida.
#language = "Spanish"  # Comentar para Error
print(language) # Descomentar para Error

#3. Genera un IndexError accediendo a un índice inexistente de una lista.
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(my_list[5]) # Descomentar para Error

#4. Genera un ModuleNotFoundError al importar un módulo inexistente.
#import maths # Descomentar para Error

#5. Genera un AttributeError accediendo a un atributo que no existe.
#print(math.PI) # Descomentar para Error

#6. Genera un KeyError al acceder a una clave inexistente de un diccionario.
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
#print(my_dict["Apelido"]) # Descomentar para Error

#7. Genera un TypeError usando tipos incorrectos (índice string en lista).
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(my_list["0"]) # Descomentar para Error

#8. Genera un ImportError al importar una función que no existe desde un módulo.
# from math import PI # Descomentar para Error

#9. Genera un ValueError intentando convertir un string no numérico a entero.
#my_int = int("10 Años") # Descomentar para Error

#10. Intenta detectar si un error ocurre usando tryexcept con un KeyError.
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
try:
    print(my_dict["Apelido"])
except KeyError:
    print("Error: La clave 'Apelido' no existe en el diccionario.")
