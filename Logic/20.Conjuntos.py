"""
Realiza un programa python que muestre ejemplos de las siguientes operaciones con conjuntos:
* Unión
* Intersección
* Diferencia
* Diferencia simétrica
* Subconjunto
* Producto cartesiano
* Potencia de un conjunto
* Complemento de un conjunto
* Producto de conjuntos
"""
from itertools import chain, combinations, product

# Funciones para operaciones con conjuntos
def union(setA, setB):
    return setA | setB

def interseccion(setA, setB):
    return setA & setB

def diferencia(setA, setB):
    return setA - setB

def diferencia_simetrica(setA, setB):
    return setA ^ setB

def es_subconjunto(subset, setA):
    return subset.issubset(setA)

def producto_cartesiano(setA, setB):
    return set(product(setA, setB))

def potencia_conjunto(setA):
    return set(frozenset(s) for s in chain.from_iterable(combinations(setA, r) for r in range(len(setA) + 1)))

def complemento(setA, universo):
    return universo - setA

def producto_de_conjuntos(setA, setB):
    return {a * b for a in setA for b in setB}

# Ejemplo de uso
A = {1, 2, 3}
B = {3, 4, 5}
universo = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("Unión:", union(A, B))
print("Intersección:", interseccion(A, B))
print("Diferencia A - B:", diferencia(A, B))
print("Diferencia simétrica:", diferencia_simetrica(A, B))
print("¿A es subconjunto de B?", es_subconjunto(A, B))
print("Producto cartesiano:", producto_cartesiano(A, B))
print("Potencia de A:", potencia_conjunto(A))
print("Complemento de A:", complemento(A, universo))
print("Producto de conjuntos:", producto_de_conjuntos(A, B))
