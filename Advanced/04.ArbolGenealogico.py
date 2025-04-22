"""
* EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
"""
class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.pareja_id = None
        self.hijos_ids = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"


class ArbolGenealogico:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, id, nombre):
        if id in self.personas:
            print("⚠️ Ya existe una persona con ese ID.")
            return
        self.personas[id] = Persona(id, nombre)
        print(f"✅ Persona '{nombre}' añadida.")

    def eliminar_persona(self, id):
        if id not in self.personas:
            print("⚠️ Persona no encontrada.")
            return

        # Eliminar de pareja y de hijos
        for persona in self.personas.values():
            if persona.pareja_id == id:
                persona.pareja_id = None
            if id in persona.hijos_ids:
                persona.hijos_ids.remove(id)

        del self.personas[id]
        print(f"🗑️ Persona con ID {id} eliminada.")

    def asignar_pareja(self, id1, id2):
        if id1 not in self.personas or id2 not in self.personas:
            print("⚠️ Uno de los ID no existe.")
            return
        p1, p2 = self.personas[id1], self.personas[id2]
        if p1.pareja_id or p2.pareja_id:
            print("⚠️ Alguno ya tiene pareja.")
            return
        p1.pareja_id = id2
        p2.pareja_id = id1
        print(f"💍 {p1.nombre} y {p2.nombre} ahora son pareja.")

    def agregar_hijo(self, padre_id, hijo_id):
        if padre_id not in self.personas or hijo_id not in self.personas:
            print("⚠️ ID no encontrado.")
            return
        padre = self.personas[padre_id]
        hijo = self.personas[hijo_id]

        # Contar cuántos padres tiene ya
        padres = [p for p in self.personas.values() if hijo_id in p.hijos_ids]
        if len(padres) >= 2:
            print("⚠️ El hijo ya tiene dos padres.")
            return
        if hijo_id not in padre.hijos_ids:
            padre.hijos_ids.append(hijo_id)
            print(f"👶 {hijo.nombre} ha sido asignado como hijo de {padre.nombre}.")

    def imprimir_arbol(self):
        for persona in self.personas.values():
            print(f"\n🧍 {persona}")
            if persona.pareja_id:
                pareja = self.personas.get(persona.pareja_id)
                print(f"   💞 Pareja: {pareja.nombre}")
            if persona.hijos_ids:
                hijos = [self.personas[hid].nombre for hid in persona.hijos_ids]
                print(f"   👶 Hijos: {', '.join(hijos)}")

    def menu(self):
        while True:
            print("\n--- Árbol Genealógico ---")
            print("1. Añadir persona")
            print("2. Eliminar persona")
            print("3. Asignar pareja")
            print("4. Asignar hijo")
            print("5. Mostrar árbol")
            print("6. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                id = input("ID: ")
                nombre = input("Nombre: ")
                self.agregar_persona(id, nombre)

            elif opcion == "2":
                id = input("ID de la persona a eliminar: ")
                self.eliminar_persona(id)

            elif opcion == "3":
                id1 = input("ID de la primera persona: ")
                id2 = input("ID de la segunda persona: ")
                self.asignar_pareja(id1, id2)

            elif opcion == "4":
                padre_id = input("ID del padre o madre: ")
                hijo_id = input("ID del hijo: ")
                self.agregar_hijo(padre_id, hijo_id)

            elif opcion == "5":
                self.imprimir_arbol()

            elif opcion == "6":
                print("¡Hasta la próxima! 🐉")
                break

            else:
                print("❌ Opción no válida.")


# Ejecución
if __name__ == "__main__":
    arbol = ArbolGenealogico()
    arbol.menu()
