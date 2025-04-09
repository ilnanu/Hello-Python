"""
 * EJERCICIO:
 Explora el concepto de funciones de orden superior en python 
 creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""
# 1.Recibir funciones como argumentos

def aplicar_operacion(x, y, operacion):
    return operacion(x, y)

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Uso:
print(aplicar_operacion(5, 3, sumar))        # 8
print(aplicar_operacion(5, 3, multiplicar))  # 15

# 2.Devolver una función

def crear_saludo(tipo):
    def saludo_formal(nombre):
        return f"Buenos días, {nombre}."

    def saludo_informal(nombre):
        return f"¡Hey, {nombre}!"

    return saludo_formal if tipo == "formal" else saludo_informal

# Uso:
saludo = crear_saludo("informal")
print(saludo("Ana"))  # ¡Hey, Ana!

saludo = crear_saludo("formal")
print(saludo("Carlos"))  # Buenos días, Carlos.

# 3.Combinar funciones como datos

def procesar_lista(lista, funcion):
    return [funcion(x) for x in lista]

doble = lambda x: x * 2
cuadrado = lambda x: x ** 2

nums = [1, 2, 3, 4]

print(procesar_lista(nums, doble))     # [2, 4, 6, 8]
print(procesar_lista(nums, cuadrado))  # [1, 4, 9, 16]


"""
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 """

from datetime import datetime
from statistics import mean
from itertools import chain


# Lista de estudiantes
estudiantes = [
    {
        "nombre": "Ana",
        "nacimiento": "2005-06-10",
        "calificaciones": [8.5, 9.0, 7.5]
    },
    {
        "nombre": "Luis",
        "nacimiento": "2004-02-20",
        "calificaciones": [9.5, 9.0, 10.0]
    },
    {
        "nombre": "María",
        "nacimiento": "2006-11-05",
        "calificaciones": [6.0, 7.0, 5.5]
    },
    {
        "nombre": "Pedro",
        "nacimiento": "2003-09-15",
        "calificaciones": [10.0, 10.0, 9.5]
    }
]

# Validación de calificaciones
for est in estudiantes:
    est['calificaciones'] = list(filter(lambda x: 0 <= x <= 10, est['calificaciones']))

# 1. Promedio de calificaciones
promedios = list(map(lambda e: {
    "nombre": e['nombre'],
    "promedio": round(mean(e['calificaciones']), 2)
}, estudiantes))

print("\n🎓 Promedios de calificaciones:")
for p in promedios:
    print(f"{p['nombre']}: {p['promedio']}")

# 2. Mejores estudiantes (promedio >= 9)
mejores = list(filter(lambda e: mean(e['calificaciones']) >= 9, estudiantes))
print("\n🏅 Mejores estudiantes (promedio >= 9):")
for e in mejores:
    print(f"{e['nombre']}")

# 3. Estudiantes ordenados desde el más joven
ordenados_por_edad = sorted(estudiantes, key=lambda e: datetime.strptime(e['nacimiento'], "%Y-%m-%d"), reverse=True)
print("\n📅 Estudiantes ordenados por edad (de más joven a mayor):")
for e in ordenados_por_edad:
    print(f"{e['nombre']} - {e['nacimiento']}")

# 4. Mayor calificación entre todos
todas_las_calificaciones = list(chain.from_iterable(map(lambda e: e['calificaciones'], estudiantes)))
mayor_calificacion = max(todas_las_calificaciones)
print(f"\n🏆 Mayor calificación entre todos: {mayor_calificacion}")
