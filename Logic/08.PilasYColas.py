# Utilizando una pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedes navegar a una página o indicarle que te quieresdesplazar aledante o atrás, mostrando en cada caso el nombre de la web
# Las palabras "adelante", "atras" desencadena esta acción, el resto se interpreta como el nombre de una nueva web.

# Importamos la librería de pilas
from collections import deque

# Creamos una pila vacía
pila = deque()

# Creamos una variable para almacenar la página actual

pagina_actual = ""
# Creamos un bucle infinito
while True:
    # Pedimos al usuario que introduzca un comando
    comando = input("Introduce un comando: ")
    # Si el comando es "atras"
    if comando == "atras":
        # Si la pila no está vacía
        if len(pila) > 0:
            # Sacamos el último elemento de la pila
            pagina_actual = pila.pop()
            # Mostramos la página actual
            print("Página actual:", pagina_actual)
        # Si la pila está vacía
        else:
            # Mostramos un mensaje de error
            print("No hay páginas para retroceder")
    # Si el comando es "adelante"
    elif comando == "adelante":
        # Si la página actual no está vacía
        if pagina_actual != "":
            # Añadimos la página actual a la pila
            pila.append(pagina_actual)
            # Mostramos un mensaje de error
            print("No hay páginas para avanzar")
    # Si el comando no es "atras" ni "adelante"
    else:
        # Si la página actual no está vacía
        if pagina_actual != "":
            # Añadimos la página actual a la pila
            pila.append(pagina_actual)
        # Actualizamos la página actual con el comando introducido
        pagina_actual = comando
        # Mostramos la página actual
        print("Página actual:", pagina_actual)

# Ejecuta el programa y prueba a navegar entre diferentes páginas web utilizando los comandos "adelante" y "atras".
# Introduce el nombre de una página web para navegar a ella.
# Por ejemplo, puedes probar a introducir los siguientes comandos:
# google.com
# youtube.com
# facebook.com

# ¿Qué ocurre si introduces el comando "adelante" cuando no hay ninguna página actual?
# ¿Qué ocurre si introduces el comando "atras" cuando no hay ninguna página en la pila?
# ¿Qué ocurre si introduces el comando "atras" después de haber introducido una página web?

# Respuestas:
# Si introduces el comando "adelante" cuando no hay ninguna página actual, el programa mostrará el mensaje "No hay páginas para avanzar".
# Si introduces el comando "atras" cuando no hay ninguna página en la pila, el programa mostrará el mensaje "No hay páginas para retroceder".
# Si introduces el comando "atras" después de haber introducido una página web, la página actual se moverá a la pila y se mostrará la página anterior.


# Utilizando colas y cadenas de texto, simula el mecanismo de una cola de impresión. Crea un programa en el que puedes añadir trabajos a la cola, mostrar el trabajo que se está imprimiendo y eliminar el trabajo que se ha impreso.
# Las palabras "imprimir", "siguiente" y "eliminar" desencadenan estas acciones, el resto se interpreta como un trabajo a añadir a la cola.

# Importamos la librería de colas
from collections import deque

# Creamos una cola vacía
cola = deque()

# Creamos un bucle infinito
while True:
    # Pedimos al usuario que introduzca un comando
    comando = input("Introduce un comando: ")
    # Si el comando es "imprimir"
    if comando == "imprimir":
        # Si la cola no está vacía
        if len(cola) > 0:
            # Sacamos el primer
            trabajo = cola.popleft()
            # Mostramos el trabajo que se está imprimiendo
            print("Imprimiendo:", trabajo)
        # Si la cola está vacía
        else:
            # Mostramos un mensaje de error
            print("No hay trabajos para imprimir")
    # Si el comando es "siguiente"
    elif comando == "siguiente":
        # Si la cola no está vacía
        if len(cola) > 0:
            # Mostramos el siguiente trabajo a imprimir
            print("Siguiente trabajo:", cola[0])
        # Si la cola está vacía
        else:
            # Mostramos un mensaje de error
            print("No hay trabajos para imprimir")
    # Si el comando es "eliminar"
    elif comando == "eliminar":
        # Si la cola no está vacía
        if len(cola) > 0:
            # Sacamos el primer trabajo de la cola
            trabajo = cola.popleft()
            # Mostramos un mensaje de éxito 
            print("Trabajo eliminado:", trabajo)
        # Si la cola está vacía
        else:
            # Mostramos un mensaje de error
            print("No hay trabajos para eliminar")
    # Si el comando no es "imprimir", "siguiente" ni "eliminar"
    else:
        # Añadimos el trabajo a la cola
        cola.append(comando)
        # Mostramos un mensaje de éxito
        print("Trabajo añadido a la cola:", comando)

# Ejecuta el programa y prueba a añadir trabajos a la cola de impresión utilizando el comando "imprimir".
# Utiliza el comando "siguiente" para ver cuál es el siguiente trabajo a imprimir.
# Utiliza el comando "eliminar" para eliminar el trabajo que se ha impreso.
# Por ejemplo, puedes probar a introducir los siguientes comandos:

# imprimir
# siguiente
# eliminar
# imprimir
# siguiente



