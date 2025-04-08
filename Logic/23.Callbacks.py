"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""

def procesar_lista(lista, callback):
    """Aplica una función (callback) a cada elemento de la lista."""
    resultado = []
    for elemento in lista:
        resultado.append(callback(elemento))
    return resultado

# Funciones de ejemplo para usar como callbacks
def al_cuadrado(x):
    return x * x

def al_doble(x):
    return x * 2

# Uso
numeros = [1, 2, 3, 4, 5]

print("Aplicando al_cuadrado:")
print(procesar_lista(numeros, al_cuadrado))  # [1, 4, 9, 16, 25]

print("Aplicando al_doble:")
print(procesar_lista(numeros, al_doble))     # [2, 4, 6, 8, 10]

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
"""
import time
import random

def procesar_pedido(plato, on_confirmacion, on_listo, on_entrega):
    print(f"\n🔔 Recibido pedido de: {plato}")

    # Confirmación del pedido
    on_confirmacion(plato)
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)

    # Plato listo
    on_listo(plato)
    tiempo_entrega = random.randint(1, 5)
    time.sleep(tiempo_entrega)

    # Plato entregado
    on_entrega(plato)

# Callbacks

def confirmar_pedido(plato):
    print(f"✅ Pedido confirmado: {plato}")

def plato_listo(plato):
    print(f"🍽️ El plato '{plato}' está listo para servir.")

def entregar_pedido(plato):
    print(f"📦 Pedido '{plato}' ha sido entregado al cliente.\n")

# Simulación de varios pedidos
if __name__ == "__main__":
    pedidos = ["Pizza Margarita", "Ensalada César", "Sushi", "Hamburguesa"]
    for plato in pedidos:
        procesar_pedido(plato, confirmar_pedido, plato_listo, entregar_pedido)
