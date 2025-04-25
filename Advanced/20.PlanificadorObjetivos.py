"""
/*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */
"""
import os

class Objetivo:
    def __init__(self, meta, cantidad, unidades, plazo):
        self.meta = meta
        self.cantidad = cantidad
        self.unidades = unidades
        self.plazo = plazo

    def calcular_plan(self):
        plan_mensual = self.cantidad // self.plazo  # División entera
        if self.cantidad % self.plazo != 0:
            plan_mensual += 1  # Si no es divisible, ajusta para el último mes
        return plan_mensual

    def mostrar_plan(self):
        plan_mensual = self.calcular_plan()
        plan_total = self.cantidad
        return f"[ ] 1. {self.meta} ({plan_mensual} {self.unidades}/mes). Total: {plan_total}."


class GestorObjetivos:
    def __init__(self):
        self.objetivos = []

    def añadir_objetivo(self):
        if len(self.objetivos) >= 10:
            print("¡Ya has alcanzado el número máximo de objetivos (10)! No puedes añadir más.")
            return

        meta = input("Meta: ")
        cantidad = int(input("Cantidad: "))
        unidades = input("Unidades: ")
        plazo = int(input("Plazo (en meses, máximo 12): "))

        if plazo > 12:
            print("El plazo no puede ser superior a 12 meses.")
            return

        objetivo = Objetivo(meta, cantidad, unidades, plazo)
        self.objetivos.append(objetivo)
        print(f"Objetivo '{meta}' añadido correctamente.")

    def calcular_plan_detallado(self):
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        plan_detallado = ""
        for mes in meses[:min(12, max([obj.plazo for obj in self.objetivos]))]:
            plan_detallado += f"\n{mes}:\n"
            for objetivo in self.objetivos:
                if objetivo.plazo >= meses.index(mes) + 1:  # Si el objetivo se cumple en ese mes
                    plan_detallado += f"  {objetivo.mostrar_plan()}\n"
        return plan_detallado

    def guardar_plan(self, plan_detallado):
        with open("plan_detallado.txt", "w") as file:
            file.write(plan_detallado)
        print("Plan guardado en 'plan_detallado.txt'.")

    def mostrar_objetivos(self):
        if not self.objetivos:
            print("No tienes objetivos añadidos.")
            return

        for idx, obj in enumerate(self.objetivos, 1):
            print(f"{idx}. {obj.meta} - {obj.cantidad} {obj.unidades} en {obj.plazo} meses")

def ejecutar_programa():
    gestor = GestorObjetivos()

    while True:
        print("\nGestor de Objetivos del Nuevo Año")
        print("1. Añadir Objetivo")
        print("2. Calcular Plan Detallado")
        print("3. Guardar Plan Detallado")
        print("4. Ver Objetivos")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            gestor.añadir_objetivo()
        elif opcion == "2":
            plan_detallado = gestor.calcular_plan_detallado()
            print(plan_detallado)
        elif opcion == "3":
            plan_detallado = gestor.calcular_plan_detallado()
            gestor.guardar_plan(plan_detallado)
        elif opcion == "4":
            gestor.mostrar_objetivos()
        elif opcion == "5":
            print("¡Hasta el próximo año! ¡Que cumplas tus objetivos!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    ejecutar_programa()
