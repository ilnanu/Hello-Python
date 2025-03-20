# Implementa dos clases que representen las estructuras de Pila y Cola. Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        print(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        print(self.items)

# Ejemplo de uso de la clase Pila
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Contenido de la pila después de apilar 1, 2, 3:")
pila.imprimir()

print("Elemento desapilado:", pila.desapilar())
print("Contenido de la pila después de desapilar:")
pila.imprimir()

print("Tamaño de la pila:", pila.tamano())
print("¿La pila está vacía?", pila.esta_vacia())

# Ejemplo de uso de la clase Cola
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Contenido de la cola después de encolar 1, 2, 3:")
cola.imprimir()

print("Elemento desencolado:", cola.desencolar())
print("Contenido de la cola después de desencolar:")
cola.imprimir()

print("Tamaño de la cola:", cola.tamano())
print("¿La cola está vacía?", cola.esta_vacia())
