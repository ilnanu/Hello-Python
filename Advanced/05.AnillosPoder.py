"""
/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */
"""
import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def buscar_reparto(total_anillos):
    total_sin_sauron = total_anillos - 1
    encontrado = False

    for elfos in range(1, total_sin_sauron, 2):  # números impares
        for enanos in range(2, total_sin_sauron - elfos):
            if not es_primo(enanos):
                continue
            hombres = total_sin_sauron - elfos - enanos
            if hombres >= 0 and hombres % 2 == 0:
                print("\n🎉 Reparto posible:")
                print(f"🧝 Elfos: {elfos}")
                print(f"⛏️ Enanos: {enanos}")
                print(f"🧔 Hombres: {hombres}")
                print(f"👁️ Sauron: 1")
                encontrado = True
                return

    if not encontrado:
        print("❌ No hay una combinación válida para repartir los anillos.")

# --- Interacción principal ---

if __name__ == "__main__":
    try:
        total = int(input("🔢 Introduce el número total de anillos: "))
        if total < 4:
            print("⚠️ Debe haber al menos 4 anillos para hacer un reparto.")
        else:
            buscar_reparto(total)
    except ValueError:
        print("⚠️ Por favor, introduce un número válido.")
