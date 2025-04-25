"""
/*
 * EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
 */
 """
import subprocess
import os

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
        if resultado.stdout:
            print(resultado.stdout)
        if resultado.stderr:
            print("⚠️", resultado.stderr)
    except Exception as e:
        print("❌ Error ejecutando el comando:", e)

def establecer_directorio():
    ruta = input("📁 Introduce el path del directorio de trabajo: ").strip()
    if os.path.isdir(ruta):
        os.chdir(ruta)
        print(f"✅ Directorio cambiado a: {os.getcwd()}")
    else:
        print("❌ El directorio no existe.")

def crear_repositorio():
    ejecutar_comando("git init")

def crear_rama():
    nombre = input("🌿 Nombre de la nueva rama: ").strip()
    ejecutar_comando(f"git branch {nombre}")

def cambiar_rama():
    nombre = input("🔀 Nombre de la rama a cambiar: ").strip()
    ejecutar_comando(f"git checkout {nombre}")

def ficheros_pendientes():
    ejecutar_comando("git status")

def hacer_commit():
    mensaje = input("✏️ Escribe el mensaje del commit: ").strip()
    ejecutar_comando("git add .")
    ejecutar_comando(f'git commit -m "{mensaje}"')

def mostrar_historial():
    ejecutar_comando("git log --oneline")

def eliminar_rama():
    nombre = input("🧨 Nombre de la rama a eliminar: ").strip()
    ejecutar_comando(f"git branch -d {nombre}")

def establecer_remoto():
    url = input("🔗 URL del repositorio remoto: ").strip()
    ejecutar_comando(f"git remote add origin {url}")

def hacer_pull():
    rama = input("⬇️ Rama desde la que hacer pull (ej. main): ").strip()
    ejecutar_comando(f"git pull origin {rama}")

def hacer_push():
    rama = input("⬆️ Rama a la que hacer push (ej. main): ").strip()
    ejecutar_comando(f"git push origin {rama}")

def mostrar_menu():
    print("""
========= 🌌 GitHub Universe CLI 🌌 =========
1.  Establecer directorio de trabajo
2.  Crear un nuevo repositorio
3.  Crear una nueva rama
4.  Cambiar de rama
5.  Mostrar ficheros pendientes de hacer commit
6.  Hacer commit
7.  Mostrar el historial de commits
8.  Eliminar rama
9.  Establecer repositorio remoto
10. Hacer pull
11. Hacer push
12. Salir
============================================
""")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-12): ").strip()
        match opcion:
            case "1": establecer_directorio()
            case "2": crear_repositorio()
            case "3": crear_rama()
            case "4": cambiar_rama()
            case "5": ficheros_pendientes()
            case "6": hacer_commit()
            case "7": mostrar_historial()
            case "8": eliminar_rama()
            case "9": establecer_remoto()
            case "10": hacer_pull()
            case "11": hacer_push()
            case "12":
                print("👋 ¡Hasta luego, GitHubnauta!")
                break
            case _: print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
