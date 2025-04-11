"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""
class Decorador:
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        print("🔄 Antes de ejecutar la función.")
        resultado = self.funcion(*args, **kwargs)
        print("✅ Después de ejecutar la función.")
        return resultado
@Decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Ejemplo de uso
if __name__ == "__main__":
    saludar("Juan")
    print("\n🔄 Decorador aplicado a la función 'saludar'.")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""
class ContadorLlamadas:
    def __init__(self, funcion):
        self.funcion = funcion
        self.contador = 0

    def __call__(self, *args, **kwargs):
        self.contador += 1
        print(f"🔄 Llamada número: {self.contador}")
        return self.funcion(*args, **kwargs)
@ContadorLlamadas
def sumar(a, b):
    return a + b
# Ejemplo de uso
if __name__ == "__main__":
    print(sumar(3, 4))
    print(sumar(5, 6))
    print(sumar(7, 8))
    print("\n🔄 Decorador 'ContadorLlamadas' aplicado a la función 'sumar'.")