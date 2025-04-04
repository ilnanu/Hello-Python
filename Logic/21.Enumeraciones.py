"""
Crea un pequeño sistema de gestión del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes características:
* El pedido tiene un ID único y un estado.
* El estado es un enumerado que puede ser PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
* Implementa las funciones que sirvan para modificar el estado:
    * Cambiar el estado a ENVIADO.
    * Cambiar el estado a ENTREGADO.
    * Cambiar el estado a CANCELADO.
    * Cambiar el estado a PENDIENTE.
    * Cambiar el estado a un valor inválido (debería lanzar un error).
    (establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
* Implementa un método para mostrar el estado actual del pedido.
* Crea diferentes pedidos y muestra cómo se interactua con ellos.
"""
from enum import Enum, auto
import uuid

class EstadoPedido(Enum):
    PENDIENTE = auto()
    ENVIADO = auto()
    ENTREGADO = auto()
    CANCELADO = auto()

class Pedido:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.estado = EstadoPedido.PENDIENTE

    def mostrar_estado(self):
        print(f"Pedido {self.id[:8]} - Estado actual: {self.estado.name}")

    def cambiar_estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, EstadoPedido):
            raise ValueError("Estado inválido. Debe ser una instancia de EstadoPedido.")

        if nuevo_estado == EstadoPedido.ENVIADO:
            if self.estado != EstadoPedido.PENDIENTE:
                raise ValueError("Solo se puede enviar un pedido que esté PENDIENTE.")

        elif nuevo_estado == EstadoPedido.ENTREGADO:
            if self.estado != EstadoPedido.ENVIADO:
                raise ValueError("Solo se puede entregar un pedido que haya sido ENVIADO.")

        elif nuevo_estado == EstadoPedido.CANCELADO:
            if self.estado == EstadoPedido.ENTREGADO:
                raise ValueError("No se puede cancelar un pedido ya ENTREGADO.")

        elif nuevo_estado == EstadoPedido.PENDIENTE:
            if self.estado != EstadoPedido.CANCELADO:
                raise ValueError("Solo se puede volver a estado PENDIENTE desde CANCELADO.")

        self.estado = nuevo_estado
        print(f"El estado del pedido {self.id[:8]} ha cambiado a: {self.estado.name}")

# Demostración del sistema de gestión de pedidos
if __name__ == "__main__":
    pedido1 = Pedido()
    pedido2 = Pedido()

    pedido1.mostrar_estado()
    pedido1.cambiar_estado(EstadoPedido.ENVIADO)
    pedido1.cambiar_estado(EstadoPedido.ENTREGADO)
    pedido1.mostrar_estado()

    pedido2.mostrar_estado()
    pedido2.cambiar_estado(EstadoPedido.CANCELADO)
    pedido2.mostrar_estado()
    try:
        pedido2.cambiar_estado(EstadoPedido.ENTREGADO)
    except ValueError as e:
        print("Error:", e)

    try:
        pedido2.cambiar_estado("REEMBOLSADO")  # Estado inválido
    except ValueError as e:
        print("Error:", e)

    try:
        pedido2.cambiar_estado(EstadoPedido.PENDIENTE)  # válido desde CANCELADO
        pedido2.mostrar_estado()
    except ValueError as e:
        print("Error:", e)
