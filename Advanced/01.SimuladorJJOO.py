"""
* EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""
import random
from collections import defaultdict

class Participante:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.participantes = []
        self.resultados = []

    def agregar_participante(self, participante):
        self.participantes.append(participante)

    def simular(self):
        if len(self.participantes) < 3:
            print(f"No hay suficientes participantes en {self.nombre} para simular.")
            return False
        self.resultados = random.sample(self.participantes, len(self.participantes))
        return True

    def obtener_podio(self):
        return self.resultados[:3]

class JuegosOlimpicos:
    def __init__(self):
        self.eventos = []
        self.paises_medallas = defaultdict(lambda: {'oro': 0, 'plata': 0, 'bronce': 0})

    def registrar_evento(self, nombre):
        self.eventos.append(Evento(nombre))

    def listar_eventos(self):
        for i, evento in enumerate(self.eventos):
            print(f"{i + 1}. {evento.nombre} ({len(evento.participantes)} participantes)")

    def registrar_participante(self, evento_index, nombre, pais):
        if 0 <= evento_index < len(self.eventos):
            self.eventos[evento_index].agregar_participante(Participante(nombre, pais))

    def simular_eventos(self):
        for evento in self.eventos:
            if evento.simular():
                print(f"\nEvento: {evento.nombre}")
                podio = evento.obtener_podio()
                medallas = ['oro', 'plata', 'bronce']
                for idx, participante in enumerate(podio):
                    self.paises_medallas[participante.pais][medallas[idx]] += 1
                    print(f"{medallas[idx].capitalize()}: {participante.nombre} ({participante.pais})")

    def mostrar_ranking(self):
        print("\nRanking de países por medallas:")
        ranking = sorted(self.paises_medallas.items(), key=lambda p: (p[1]['oro'], p[1]['plata'], p[1]['bronce']), reverse=True)
        for pais, medallas in ranking:
            print(f"{pais} - Oro: {medallas['oro']}, Plata: {medallas['plata']}, Bronce: {medallas['bronce']}")

def menu():
    juegos = JuegosOlimpicos()
    while True:
        print("\n--- JJOO París 2024 ---")
        print("1. Registrar evento")
        print("2. Registrar participante")
        print("3. Simular eventos")
        print("4. Mostrar ranking de países")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del evento: ")
            juegos.registrar_evento(nombre)
        elif opcion == '2':
            juegos.listar_eventos()
            idx = int(input("Seleccione evento por número: ")) - 1
            nombre = input("Nombre del participante: ")
            pais = input("País: ")
            juegos.registrar_participante(idx, nombre, pais)
        elif opcion == '3':
            juegos.simular_eventos()
        elif opcion == '4':
            juegos.mostrar_ranking()
        elif opcion == '5':
            print("¡Gracias por usar el simulador JJOO!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
