"""
Escribe el mayor número de mecanismos que posee python para iterar valores.
"""
import itertools
from functools import reduce

print("\n1. Bucle for con lista:")
for i in [1, 2, 3]:
    print(i)

print("\n2. Bucle while:")
i = 0
while i < 3:
    print(i)
    i += 1

print("\n3. Iteración con range:")
for i in range(1, 5, 2):
    print(i)

print("\n4. Iteración sobre diccionario:")
diccionario = {"a": 1, "b": 2}
for clave, valor in diccionario.items():
    print(clave, valor)

print("\n5. Enumerate:")
lista = ['a', 'b', 'c']
for i, valor in enumerate(lista):
    print(i, valor)

print("\n6. Zip:")
nombres = ['Ana', 'Luis']
edades = [25, 30]
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

print("\n7. List Comprehension:")
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

print("\n8. Set y Dict Comprehension:")
conjunto = {x for x in range(5)}
print(conjunto)
dicc = {x: x**2 for x in range(3)}
print(dicc)

print("\n9. Iteradores y Generadores:")
lista = iter([1, 2, 3])
print(next(lista))
def generador():
    for i in range(3):
        yield i
for valor in generador():
    print(valor)

print("\n10. Funciones Funcionales:")
print(list(map(lambda x: x*2, [1, 2, 3])))
print(list(filter(lambda x: x % 2 == 0, range(5))))
print(reduce(lambda x, y: x + y, [1, 2, 3]))

print("\n11. Itertools:")
print(list(itertools.islice(itertools.count(10, 2), 5)))
print(list(itertools.islice(itertools.cycle([1, 2, 3]), 7)))
print(list(itertools.permutations([1, 2, 3])))

print("\n12. Leer archivo línea por línea:")
try:
    with open('archivo.txt') as f:
        for linea in f:
            print(linea.strip())
except FileNotFoundError:
    print("archivo.txt no encontrado, omitiendo este paso.")
