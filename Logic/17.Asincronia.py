"""
Crea un programa en javascript capaz de ejecutar de manera asíncrona una función que tardará en finalizar un número concreto de segundos parametrizables.
También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará su ejecución y cuando finalia.
"""

import asyncio

async def tarea(nombre: str, duracion: int):
    print(f"[{nombre}] Iniciando tarea. Duración: {duracion} segundos.")
    await asyncio.sleep(duracion)
    print(f"[{nombre}] Tarea finalizada tras {duracion} segundos.")

async def main():
    # Ejecutar varias tareas asíncronas
    tareas = [
        tarea("Tarea 1", 3),
        tarea("Tarea 2", 5),
        tarea("Tarea 3", 2)
    ]
    await asyncio.gather(*tareas)

if __name__ == "__main__":
    asyncio.run(main())

"""
Utilizando el concepto de asincronía y la función anterior, crea el siguiente programa que ejecuta en este orden
* Una función C que dura 3 segundos
* Una función B que dura 2 segundos
* Una función A que dura 1 segundo
* Una función D que dura 1 segundo
* Las funciones C, B y A se ejecutan en paralelo.
* La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""
import asyncio

async def tarea(nombre: str, duracion: int):
    print(f"[{nombre}] Iniciando tarea. Duración: {duracion} segundos.")
    await asyncio.sleep(duracion)
    print(f"[{nombre}] Tarea finalizada tras {duracion} segundos.")

async def main():
    # Ejecutar C, B y A en paralelo
    tareas_paralelas = [
        tarea("C", 3),
        tarea("B", 2),
        tarea("A", 1)
    ]
    await asyncio.gather(*tareas_paralelas)
    
    # Ejecutar D solo después de que C, B y A hayan finalizado
    await tarea("D", 1)

if __name__ == "__main__":
    asyncio.run(main())

