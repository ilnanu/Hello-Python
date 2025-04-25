"""
/*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */
"""
import random
import time
from typing import List

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def restablecer_salud(self):
        self.salud = 100

    def __str__(self):
        return f"{self.nombre} [VEL: {self.velocidad} | ATK: {self.ataque} | DEF: {self.defensa}]"

def batalla(l1: Luchador, l2: Luchador) -> Luchador:
    print(f"\n🔔 ¡Comienza la batalla entre {l1.nombre} y {l2.nombre}!")
    l1.restablecer_salud()
    l2.restablecer_salud()

    atacante, defensor = (l1, l2) if l1.velocidad >= l2.velocidad else (l2, l1)
    print(f"⚡ {atacante.nombre} ataca primero por su mayor velocidad.")

    while l1.salud > 0 and l2.salud > 0:
        if random.random() <= 0.2:
            print(f"🛡️ {defensor.nombre} esquiva el ataque de {atacante.nombre}!")
        else:
            if atacante.ataque > defensor.defensa:
                dano = atacante.ataque - defensor.defensa
            else:
                dano = int(atacante.ataque * 0.1)
            defensor.salud -= dano
            print(f"💥 {atacante.nombre} ataca a {defensor.nombre} causando {dano} de daño. ({defensor.salud} de salud restante)")

        atacante, defensor = defensor, atacante
        time.sleep(0.5)

    ganador = l1 if l1.salud > 0 else l2
    print(f"🏆 ¡{ganador.nombre} gana la batalla!\n")
    return ganador

def es_potencia_de_2(n):
    return (n != 0) and (n & (n - 1) == 0)

def torneo(luchadores: List[Luchador]):
    if not es_potencia_de_2(len(luchadores)):
        print("❌ El número de luchadores debe ser una potencia de 2 (2, 4, 8, 16, ...)")
        return

    ronda = 1
    while len(luchadores) > 1:
        print(f"\n🔶 RONDA {ronda} 🔶")
        random.shuffle(luchadores)
        ganadores = []
        for i in range(0, len(luchadores), 2):
            ganador = batalla(luchadores[i], luchadores[i+1])
            ganadores.append(ganador)
        luchadores = ganadores
        ronda += 1

    print(f"\n🎉 ¡El campeón del torneo es {luchadores[0].nombre}!")
    print("🥇 ¡Dragon Ball Sparking! ZERO Torneo Finalizado 🐉")

# 🧙‍♂️ Luchadores de ejemplo
luchadores = [
    Luchador("Goku", 90, 85, 70),
    Luchador("Vegeta", 85, 90, 65),
    Luchador("Gohan", 75, 80, 60),
    Luchador("Piccolo", 70, 75, 80),
    Luchador("Trunks", 80, 78, 68),
    Luchador("Freezer", 60, 88, 72),
    Luchador("Cell", 65, 82, 75),
    Luchador("Majin Buu", 55, 95, 85),
]

# 🏁 Iniciar torneo
torneo(luchadores)
