"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""
# ❌ Ejemplo INCORRECTO (violando DIP)

# Módulo de alto nivel depende directamente de un módulo de bajo nivel

class MotorGasolina:
    def encender(self):
        print("Motor de gasolina encendido")

class Coche:
    def __init__(self):
        self.motor = MotorGasolina()  # 😬 dependencia directa

    def arrancar(self):
        self.motor.encender()



# ✅ Ejemplo CORRECTO (cumpliendo DIP)

from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorGasolina(Motor):
    def encender(self):
        print("Motor de gasolina encendido")

class MotorElectrico(Motor):
    def encender(self):
        print("Motor eléctrico encendido")

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor  # ✅ se inyecta la dependencia

    def arrancar(self):
        self.motor.encender()

# Crear coches con diferentes motores sin modificar la clase Coche
motor1 = MotorGasolina()
motor2 = MotorElectrico()

coche1 = Coche(motor1)
coche2 = Coche(motor2)

coche1.arrancar()  # Motor de gasolina encendido
coche2.arrancar()  # Motor eléctrico encendido

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
"""

from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class EmailNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"[Email] Enviando: {mensaje}")

class SMSNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"[SMS] Enviando: {mensaje}")

class PushNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"[Push] Enviando: {mensaje}")

class SistemaNotificaciones:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador  # ✅ depende de la abstracción

    def notificar(self, mensaje: str):
        self.notificador.enviar(mensaje)

# Podemos inyectar cualquier tipo de notificador sin modificar el sistema

email = EmailNotificador()
sms = SMSNotificador()
push = PushNotificador()

sistema_email = SistemaNotificaciones(email)
sistema_sms = SistemaNotificaciones(sms)
sistema_push = SistemaNotificaciones(push)

sistema_email.notificar("Tu pedido ha sido enviado.")
sistema_sms.notificar("Código de verificación: 123456")
sistema_push.notificar("¡Nueva actualización disponible!")
