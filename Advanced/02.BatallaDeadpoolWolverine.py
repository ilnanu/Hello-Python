import random
import time

class Personaje:
    def __init__(self, nombre, vida, min_dano, max_dano, evasion):
        self.nombre = nombre
        self.vida = vida
        self.min_dano = min_dano
        self.max_dano = max_dano
        self.evasion = evasion  # probabilidad entre 0 y 1
        self.omitir_turno = False

    def atacar(self):
        return random.randint(self.min_dano, self.max_dano)

    def esquiva(self):
        return random.random() < self.evasion

    def recibir_dano(self, dano):
        self.vida -= dano


def simular_batalla(deadpool, wolverine):
    turno = 1
    atacante = deadpool
    defensor = wolverine

    while deadpool.vida > 0 and wolverine.vida > 0:
        print(f"\n--- Turno {turno} ---")
        time.sleep(1)

        if atacante.omitir_turno:
            print(f"{atacante.nombre} se está recuperando del daño máximo anterior y pierde este turno.")
            atacante.omitir_turno = False
        else:
            if defensor.esquiva():
                print(f"{defensor.nombre} esquivó el ataque de {atacante.nombre}!")
            else:
                dano = atacante.atacar()
                defensor.recibir_dano(dano)
                print(f"{atacante.nombre} ataca a {defensor.nombre} y causa {dano} de daño.")
                if dano == atacante.max_dano:
                    print(f"¡Daño máximo! {defensor.nombre} pierde su próximo turno para recuperarse.")
                    defensor.omitir_turno = True

        print(f"Vida de {deadpool.nombre}: {deadpool.vida} | Vida de {wolverine.nombre}: {wolverine.vida}")

        atacante, defensor = defensor, atacante
        turno += 1

    print("\n=== ¡Fin del combate! ===")
    if deadpool.vida <= 0 and wolverine.vida <= 0:
        print("Ambos héroes han caído. ¡Es un empate épico!")
    elif deadpool.vida <= 0:
        print("Wolverine gana la batalla.")
    else:
        print("Deadpool gana la batalla.")


if __name__ == "__main__":
    print("=== ¡Deadpool vs Wolverine! ===")
    vida_deadpool = int(input("Introduce la vida inicial de Deadpool: "))
    vida_wolverine = int(input("Introduce la vida inicial de Wolverine: "))

    deadpool = Personaje("Deadpool", vida_deadpool, 10, 100, 0.25)
    wolverine = Personaje("Wolverine", vida_wolverine, 10, 120, 0.20)

    simular_batalla(deadpool, wolverine)
