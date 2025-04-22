"""
/*
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23! 
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico 
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */
"""
import os

# Símbolos del laberinto
VACIO = "⬜️"
OBSTACULO = "⬛️"
MICKEY = "🐭"
SALIDA = "🚪"

# Laberinto 6x6 definido manualmente
laberinto = [
    [VACIO, OBSTACULO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, OBSTACULO, VACIO, OBSTACULO, OBSTACULO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [OBSTACULO, OBSTACULO, OBSTACULO, OBSTACULO, VACIO, OBSTACULO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, OBSTACULO, OBSTACULO, OBSTACULO, VACIO, SALIDA],
]

# Posición inicial de Mickey
mickey_pos = [0, 0]
laberinto[mickey_pos[0]][mickey_pos[1]] = MICKEY

def imprimir_laberinto():
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in laberinto:
        print(" ".join(fila))
    print()

def mover_mickey(direccion):
    dx, dy = 0, 0
    if direccion == "arriba":
        dx = -1
    elif direccion == "abajo":
        dx = 1
    elif direccion == "izquierda":
        dy = -1
    elif direccion == "derecha":
        dy = 1
    else:
        print("Dirección no válida. Usa arriba, abajo, izquierda o derecha.")
        return False

    nueva_x = mickey_pos[0] + dx
    nueva_y = mickey_pos[1] + dy

    if not (0 <= nueva_x < 6 and 0 <= nueva_y < 6):
        print("¡No puedes salirte del laberinto!")
        return False
    if laberinto[nueva_x][nueva_y] == OBSTACULO:
        print("¡Hay un obstáculo en esa dirección!")
        return False

    # Verifica si llegó a la salida
    if laberinto[nueva_x][nueva_y] == SALIDA:
        laberinto[mickey_pos[0]][mickey_pos[1]] = VACIO
        mickey_pos[0], mickey_pos[1] = nueva_x, nueva_y
        laberinto[nueva_x][nueva_y] = MICKEY
        imprimir_laberinto()
        print("¡Mickey ha escapado del laberinto! 🎉🚪")
        return True

    # Mueve a Mickey
    laberinto[mickey_pos[0]][mickey_pos[1]] = VACIO
    mickey_pos[0], mickey_pos[1] = nueva_x, nueva_y
    laberinto[nueva_x][nueva_y] = MICKEY
    return False

def juego():
    imprimir_laberinto()
    while True:
        direccion = input("¿Hacia dónde debe ir Mickey? (arriba, abajo, izquierda, derecha): ").strip().lower()
        terminado = mover_mickey(direccion)
        imprimir_laberinto()
        if terminado:
            break

if __name__ == "__main__":
    juego()
