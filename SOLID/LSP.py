"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
#❌ Ejemplo INCORRECTO (Violando LSP)
class Ave:
    def volar(self):
        print("Estoy volando")

class Pinguino(Ave):
    def volar(self):
        raise Exception("¡Los pingüinos no pueden volar!")

def hacer_volar(ave: Ave):
    ave.volar()

# Esto funciona:
hacer_volar(Ave())

# Pero esto rompe el principio LSP:
#hacer_volar(Pinguino())  # ❌ Error en tiempo de ejecución

#✅ Ejemplo CORRECTO (Aplicando LSP)
from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class Aguila(AveVoladora):
    def hacer_sonido(self):
        print("¡Kree!")

    def volar(self):
        print("El águila está volando")

class Pinguino(Ave):
    def hacer_sonido(self):
        print("¡Noot noot!")

# ✅ Ambas clases se comportan correctamente dentro de su jerarquía

def presentar_ave(ave: Ave):
    ave.hacer_sonido()

presentar_ave(Aguila())     # ✅
presentar_ave(Pinguino())   # ✅


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
"""
from abc import ABC, abstractmethod

# 1. Clase base
class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

# 2. Subclases de Vehículo
class Coche(Vehiculo):
    def acelerar(self):
        print("El coche acelera suavemente.")

    def frenar(self):
        print("El coche frena con ABS.")

class Moto(Vehiculo):
    def acelerar(self):
        print("La moto acelera rápidamente.")

    def frenar(self):
        print("La moto frena con los frenos de disco.")

class Camion(Vehiculo):
    def acelerar(self):
        print("El camión acelera lentamente debido a su peso.")

    def frenar(self):
        print("El camión frena con aire comprimido.")

# 4. Función que comprueba LSP
def probar_vehiculo(vehiculo: Vehiculo):
    print(f"\nProbando un {vehiculo.__class__.__name__}:")
    vehiculo.acelerar()
    vehiculo.frenar()

# 🧪 Prueba del cumplimiento de LSP
if __name__ == '__main__':
    vehiculos = [Coche(), Moto(), Camion()]
    for v in vehiculos:
        probar_vehiculo(v)
