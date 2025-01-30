# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
mi_tupla = (10, 20, 30, 40, 50)
print(mi_tupla)
print(type(mi_tupla))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
mi_tupla = (100, 200, 300, 400, 500)
print(mi_tupla[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
mi_tupla = (1, 2, 3)
mi_tupla = list(mi_tupla)
mi_tupla[0] = 10
mi_tupla = tuple(mi_tupla)
print(mi_tupla)

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
mi_tupla = (1, 2, 3, 3, 4, 5, 3)
print(mi_tupla.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
mi_tupla = ("Java", "Python", "JavaScript", "Python")
print(mi_tupla.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
my_tupla1 = (1, 2, 3)
my_tupla2 = (4, 5, 6)
my_tupla3 = my_tupla1 + my_tupla2
print(my_tupla3)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
my_tupla1 = (10, 20, 30, 40, 50)
my_tupla2 = my_tupla1[1:4]
print(my_tupla2)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
my_tupla1 = ("rojo", "verde", "azul")
my_tupla1 = list(my_tupla1)
my_tupla1[1] = "amarillo"
my_tupla1 = tuple(my_tupla1)
print(my_tupla1)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tupla1 = (1, 2, 3)
del my_tupla1
# print(my_tupla1) # NameError: name 'my_tupla1' is not defined

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
my_tupla1 = (100,)
print(my_tupla1)
print(type(my_tupla1))
