"""
/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */
"""
import csv
import random

def cargar_usuarios_activos(ruta_csv):
    usuarios = []

    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            if fila["status"].strip().lower() == "activo":
                usuarios.append({
                    "id": fila["id"],
                    "email": fila["email"]
                })

    return usuarios

def seleccionar_ganadores(usuarios):
    if len(usuarios) < 3:
        raise ValueError("No hay suficientes usuarios activos para seleccionar 3 ganadores distintos.")

    ganadores = random.sample(usuarios, 3)

    premios = ["Suscripción", "Descuento", "Libro"]

    return list(zip(premios, ganadores))

def mostrar_ganadores(ganadores):
    print("🎉 GANADORES DEL SORTEO MOUREDEV PRO 🎉\n")

    for premio, ganador in ganadores:
        print(f"🏆 {premio}: {ganador['email']} (ID: {ganador['id']})")

if __name__ == "__main__":
    ruta_csv = "suscriptores.csv"

    try:
        usuarios_activos = cargar_usuarios_activos(ruta_csv)
        ganadores = seleccionar_ganadores(usuarios_activos)
        mostrar_ganadores(ganadores)

    except FileNotFoundError:
        print(f"❌ El archivo '{ruta_csv}' no se encuentra.")
    except ValueError as e:
        print(f"⚠️ {str(e)}")
