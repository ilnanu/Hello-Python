import random

def generar_codigo():
    """Genera un código aleatorio de 4 caracteres con letras (A-C) y números (1-3)."""
    letras = ['A', 'B', 'C']
    numeros = ['1', '2', '3']
    elementos = letras + numeros
    codigo = random.sample(elementos, 4)
    return ''.join(codigo)

def verificar_codigo(codigo_secreto, intento):
    """Compara el código de intento con el código secreto y devuelve las pistas."""
    pistas = []
    
    for i in range(4):
        if intento[i] == codigo_secreto[i]:
            pistas.append('Correcto')
        elif intento[i] in codigo_secreto:
            pistas.append('Presente')
        else:
            pistas.append('Incorrecto')
    
    return pistas

def juego():
    """Simula el juego de adivinar el código secreto."""
    codigo_secreto = generar_codigo()
    intentos = 0
    max_intentos = 10
    
    print("Bienvenido a la adivinanza del código secreto de Papá Noel!")
    print("El código tiene 4 caracteres y está compuesto por letras (A, B, C) y números (1, 2, 3).")
    print("No hay repetidos y puedes realizar hasta 10 intentos.")
    
    while intentos < max_intentos:
        intento = input(f"Intento {intentos + 1}/{max_intentos}: Introduce el código de 4 caracteres: ").upper()
        
        # Comprobar si el intento tiene una longitud de 4 caracteres y está compuesto por caracteres válidos
        if len(intento) != 4:
            print("Error: El código debe tener exactamente 4 caracteres.")
            continue
        
        if not all(c in "ABC123" for c in intento):
            print("Error: El código solo puede contener letras A, B, C y números 1, 2, 3.")
            continue
        
        # Verificar el código y dar pistas
        pistas = verificar_codigo(codigo_secreto, intento)
        
        print("Pistas: " + " | ".join(pistas))
        
        if all(pista == 'Correcto' for pista in pistas):
            print(f"¡Felicidades! Has adivinado el código secreto: {codigo_secreto}")
            break
        
        intentos += 1
    
    if intentos == max_intentos:
        print(f"Lo siento, no has adivinado el código en {max_intentos} intentos. El código secreto era: {codigo_secreto}")

# Ejecutar el juego
if __name__ == "__main__":
    juego()
