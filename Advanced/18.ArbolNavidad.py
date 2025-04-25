"""
/*
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 * 
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 * 
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 */
"""
import random

class ArbolNavidad:
    def __init__(self, altura):
        self.altura = altura
        self.estrella = False
        self.bolas = set()  # Conjunto de posiciones de bolas
        self.luces = set()  # Conjunto de posiciones de luces
        self.tree = self.crear_arbol()

    def crear_arbol(self):
        """ Crea el árbol representado por una lista de cadenas. """
        tree = []
        for i in range(self.altura):
            espacios = ' ' * (self.altura - i - 1)
            estrellas = '*' * (2 * i + 1)
            tree.append(espacios + estrellas)
        # Tronco del árbol
        tree.append(' ' * (self.altura - 1) + '|||')
        return tree

    def dibujar_arbol(self):
        """ Dibuja el árbol con las interacciones actuales. """
        arbol_con_elementos = self.tree[:]
        
        # Agregar estrella en la copa
        if self.estrella:
            arbol_con_elementos[0] = ' ' * (self.altura - 1) + '@' + ' ' * (self.altura - 1)

        # Agregar bolas y luces en las posiciones correspondientes
        for i in range(self.altura):
            arbol_con_elementos[i] = list(arbol_con_elementos[i])
            for pos in self.bolas:
                if pos == i:
                    arbol_con_elementos[i][self.altura - 1 - (i * 2 + 1) // 2] = 'o'
            for pos in self.luces:
                if pos == i:
                    arbol_con_elementos[i][self.altura - 1 - (i * 2 + 1) // 2] = '+'
            arbol_con_elementos[i] = ''.join(arbol_con_elementos[i])

        # Mostrar árbol
        for linea in arbol_con_elementos:
            print(linea)

    def añadir_estrella(self):
        """ Añade o elimina la estrella en la copa del árbol. """
        if self.estrella:
            print("La estrella ya está en la copa del árbol.")
        else:
            self.estrella = True
            print("¡Estrella añadida en la copa del árbol!")

    def eliminar_estrella(self):
        """ Elimina la estrella en la copa del árbol. """
        if not self.estrella:
            print("La estrella ya está eliminada.")
        else:
            self.estrella = False
            print("¡Estrella eliminada!")

    def añadir_bolas(self):
        """ Añade dos bolas aleatoriamente en el árbol. """
        if len(self.bolas) + 2 > self.altura * self.altura - self.altura:
            print("No hay suficiente espacio para añadir más bolas.")
        else:
            while len(self.bolas) < len(self.bolas) + 2:
                pos = random.randint(0, self.altura - 1)
                if pos not in self.bolas:
                    self.bolas.add(pos)
            print("¡Bolas añadidas aleatoriamente!")

    def eliminar_bolas(self):
        """ Elimina dos bolas aleatoriamente. """
        if len(self.bolas) < 2:
            print("No hay suficientes bolas para eliminar.")
        else:
            for _ in range(2):
                bola = random.choice(list(self.bolas))
                self.bolas.remove(bola)
            print("¡Bolas eliminadas aleatoriamente!")

    def añadir_luces(self):
        """ Añade tres luces aleatoriamente en el árbol. """
        if len(self.luces) + 3 > self.altura * self.altura - self.altura:
            print("No hay suficiente espacio para añadir más luces.")
        else:
            while len(self.luces) < len(self.luces) + 3:
                pos = random.randint(0, self.altura - 1)
                if pos not in self.luces and pos not in self.bolas:
                    self.luces.add(pos)
            print("¡Luces añadidas aleatoriamente!")

    def eliminar_luces(self):
        """ Elimina tres luces aleatoriamente. """
        if len(self.luces) < 3:
            print("No hay suficientes luces para eliminar.")
        else:
            for _ in range(3):
                luz = random.choice(list(self.luces))
                self.luces.remove(luz)
            print("¡Luces eliminadas aleatoriamente!")

    def encender_luces(self):
        """ Enciende las luces (cambia su estado). """
        if len(self.luces) == 0:
            print("No hay luces para encender.")
        else:
            print("¡Luces encendidas!")

    def apagar_luces(self):
        """ Apaga las luces (cambia su estado). """
        if len(self.luces) == 0:
            print("No hay luces para apagar.")
        else:
            print("¡Luces apagadas!")


# Interacción con el programa
def main():
    altura = int(input("Introduce la altura del árbol de Navidad: "))
    arbol = ArbolNavidad(altura)
    
    while True:
        arbol.dibujar_arbol()
        
        print("\nOpciones:")
        print("1. Añadir estrella en la copa")
        print("2. Eliminar estrella en la copa")
        print("3. Añadir bolas")
        print("4. Eliminar bolas")
        print("5. Añadir luces")
        print("6. Eliminar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            arbol.añadir_estrella()
        elif opcion == 2:
            arbol.eliminar_estrella()
        elif opcion == 3:
            arbol.añadir_bolas()
        elif opcion == 4:
            arbol.eliminar_bolas()
        elif opcion == 5:
            arbol.añadir_luces()
        elif opcion == 6:
            arbol.eliminar_luces()
        elif opcion == 7:
            arbol.encender_luces()
        elif opcion == 8:
            arbol.apagar_luces()
        elif opcion == 9:
            print("¡Feliz Navidad!")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
