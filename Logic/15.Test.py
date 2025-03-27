# Crea una función que se encargue de sumar dos números y retornar su resultado
# Crea una función que se encargue de sumar dos números y retornar su resultado
def sumar_numeros(a, b):
    return a + b

# Ejemplo de uso
resultado = sumar_numeros(5, 3)
print(f"El resultado de la suma es: {resultado}")

# Crea un test, utilizando las herramientas propias del lenguaje, que sea capaz de determinar si esa función se ejecuta correctamente.
def test_sumar_numeros():
    resultado = sumar_numeros(5, 3)
    assert resultado == 8, f"El resultado esperado es 8 y se obtuvo {resultado}"
    print("La función 'sumar_numeros' es correcta.")

"""
Crea un diccionario con las siguientes calves y valores
clave: nombre, valor: Juan
clave: edad, valor: 30
clave: fecha_nacuimiento , valor: 12/05/1980
clave: lenguajes, valor: JavaScript, Python, Java

Crear dos test:
- Uno que determine que existen todos los campos
- Otro que determine que los datos introducidos son correctos
"""

# Diccionario con las claves y valores especificados
persona = {
    "nombre": "Juan",
    "edad": 30,
    "fecha_nacimiento": "12/05/1980",
    "lenguajes": ["JavaScript", "Python", "Java"]
}

# Test para determinar que existen todos los campos
def test_existen_todos_los_campos():
    campos_requeridos = {"nombre", "edad", "fecha_nacimiento", "lenguajes"}
    assert campos_requeridos.issubset(persona.keys()), "Faltan campos en el diccionario"
    print("Todos los campos están presentes en el diccionario.")

# Test para determinar que los datos introducidos son correctos
def test_datos_correctos():
    assert persona["nombre"] == "Juan", "El nombre no es correcto"
    assert persona["edad"] == 30, "La edad no es correcta"
    assert persona["fecha_nacimiento"] == "12/05/1980", "La fecha de nacimiento no es correcta"
    assert persona["lenguajes"] == ["JavaScript", "Python", "Java"], "Los lenguajes no son correctos"
    print("Todos los datos son correctos.")

# Ejecución de los tests
test_existen_todos_los_campos()
test_datos_correctos()
