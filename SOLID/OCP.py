"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
#❌ Ejemplo INCORRECTO (Violando OCP)
class CalculadoraDescuentos:
    def calcular(self, tipo_cliente, total):
        if tipo_cliente == "regular":
            return total * 0.95
        elif tipo_cliente == "vip":
            return total * 0.90
        elif tipo_cliente == "super_vip":
            return total * 0.85
        else:
            return total

#✅ Ejemplo CORRECTO (Aplicando OCP con polimorfismo)
from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, total):
        pass

class DescuentoRegular(EstrategiaDescuento):
    def calcular_descuento(self, total):
        return total * 0.95

class DescuentoVIP(EstrategiaDescuento):
    def calcular_descuento(self, total):
        return total * 0.90

class DescuentoSuperVIP(EstrategiaDescuento):
    def calcular_descuento(self, total):
        return total * 0.85

class CalculadoraDescuentos:
    def __init__(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def calcular(self, total):
        return self.estrategia.calcular_descuento(total)

cliente_vip = CalculadoraDescuentos(DescuentoVIP())
total_con_descuento = cliente_vip.calcular(100)
print(f"Total con descuento VIP: {total_con_descuento}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""
from abc import ABC, abstractmethod

# Interfaz para todas las operaciones
class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        pass

# Operaciones básicas
class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b

class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def ejecutar(self, a, b):
        return a * b

class Division(Operacion):
    def ejecutar(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

# ✅ Nueva operación: potencia (extensión sin modificar código anterior)
class Potencia(Operacion):
    def ejecutar(self, a, b):
        return a ** b

# Calculadora que usa operaciones
class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre in self.operaciones:
            return self.operaciones[nombre].ejecutar(a, b)
        else:
            raise ValueError(f"Operación '{nombre}' no registrada")

# 🧪 Ejemplo de uso
def main():
    calc = Calculadora()
    calc.registrar_operacion("suma", Suma())
    calc.registrar_operacion("resta", Resta())
    calc.registrar_operacion("multiplicacion", Multiplicacion())
    calc.registrar_operacion("division", Division())
    calc.registrar_operacion("potencia", Potencia())

    print("Suma:", calc.calcular("suma", 10, 5))
    print("Resta:", calc.calcular("resta", 10, 5))
    print("Multiplicacion:", calc.calcular("multiplicacion", 10, 5))
    print("Division:", calc.calcular("division", 10, 2))
    print("Potencia:", calc.calcular("potencia", 2, 3))

if __name__ == '__main__':
    main()
