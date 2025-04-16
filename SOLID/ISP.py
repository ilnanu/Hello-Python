"""
EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""
# ❌ Ejemplo INCORRECTO (Violando ISP)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def nadar(self):
        pass

class Pato(Animal):
    def volar(self):
        print("El pato está volando")

    def nadar(self):
        print("El pato está nadando")

class Perro(Animal):
    def volar(self):
        raise NotImplementedError("¡El perro no puede volar!")

    def nadar(self):
        print("El perro está nadando")


# ✅ Ejemplo CORRECTO (Aplicando ISP)
from abc import ABC, abstractmethod

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pato(Nadador, Volador):
    def nadar(self):
        print("El pato nada en el lago")

    def volar(self):
        print("El pato vuela sobre el campo")

class Perro(Nadador):
    def nadar(self):
        print("El perro nada en la piscina")

def hacer_nadar(nadador: Nadador):
    nadador.nadar()

def hacer_volar(volador: Volador):
    volador.volar()

pato = Pato()
perro = Perro()

hacer_nadar(pato)
hacer_volar(pato)
hacer_nadar(perro)
# hacer_volar(perro)  # ❌ Esto daría error porque Perro no es un Volador


"""
* DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod

# Interfaces segregadas según funcionalidad
class ImpresoraBlancoNegro(ABC):
    @abstractmethod
    def imprimir_bn(self, documento):
        pass

class ImpresoraColor(ABC):
    @abstractmethod
    def imprimir_color(self, documento):
        pass

class Escaner(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass

class Fax(ABC):
    @abstractmethod
    def enviar_fax(self, documento):
        pass

class ImpresoraBN(ImpresoraBlancoNegro):
    def imprimir_bn(self, documento):
        print(f"Imprimiendo en blanco y negro: {documento}")

class ImpresoraColorSimple(ImpresoraColor):
    def imprimir_color(self, documento):
        print(f"Imprimiendo en color: {documento}")

class ImpresoraMultifuncion(ImpresoraBlancoNegro, ImpresoraColor, Escaner, Fax):
    def imprimir_bn(self, documento):
        print(f"[MF] Imprimiendo en blanco y negro: {documento}")

    def imprimir_color(self, documento):
        print(f"[MF] Imprimiendo en color: {documento}")

    def escanear(self, documento):
        print(f"[MF] Escaneando documento: {documento}")

    def enviar_fax(self, documento):
        print(f"[MF] Enviando fax del documento: {documento}")

def probar_impresora_bn(impresora: ImpresoraBlancoNegro):
    impresora.imprimir_bn("Factura 001")

def probar_impresora_color(impresora: ImpresoraColor):
    impresora.imprimir_color("Informe de ventas")

def probar_multifuncion(impresora: Fax):
    impresora.enviar_fax("Contrato firmado")

# Crear instancias
bn = ImpresoraBN()
color = ImpresoraColorSimple()
multifuncion = ImpresoraMultifuncion()

# Probar funcionalidades
probar_impresora_bn(bn)
probar_impresora_color(color)
probar_impresora_bn(multifuncion)
probar_impresora_color(multifuncion)
probar_multifuncion(multifuncion)

# ❌ Estas no deberían tener métodos innecesarios, y así es
# probar_impresora_color(bn)  # Esto causaría error si se descomenta
