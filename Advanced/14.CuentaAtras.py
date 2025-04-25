"""
/*
 * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
 */
"""
import datetime
import time
import threading
import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cuenta_atras(fecha_objetivo_local):
    # Convertimos la fecha local a UTC
    fecha_utc = fecha_objetivo_local.astimezone(datetime.timezone.utc)
    print(f"📅 Fecha objetivo (UTC): {fecha_utc.strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        ahora_utc = datetime.datetime.now(datetime.timezone.utc)
        diferencia = fecha_utc - ahora_utc

        if diferencia.total_seconds() <= 0:
            limpiar_terminal()
            print("🚀 ¡Ha llegado el momento! ¡MoureDev Pro ya está disponible! 🎉")
            break

        dias = diferencia.days
        horas, resto = divmod(diferencia.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        limpiar_terminal()
        print("⌛ Cuenta atrás para el lanzamiento de MoureDev Pro:")
        print(f"{dias} días, {horas:02} horas, {minutos:02} minutos, {segundos:02} segundos restantes.")
        time.sleep(1)

def iniciar_cuenta_atras():
    try:
        print("Introduce la fecha y hora de finalización (hora local):")
        anio = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Día: "))
        hora = int(input("Hora (0-23): "))
        minuto = int(input("Minuto: "))
        segundo = int(input("Segundo: "))

        fecha_local = datetime.datetime(anio, mes, dia, hora, minuto, segundo)
        # Asumimos zona horaria local (sin especificar tzinfo explícito)
        fecha_local = fecha_local.astimezone()  # Lo convierte a la zona local con tzinfo
    except Exception as e:
        print("❌ Error al introducir la fecha:", e)
        return

    hilo = threading.Thread(target=cuenta_atras, args=(fecha_local,))
    hilo.start()

if __name__ == "__main__":
    iniciar_cuenta_atras()
