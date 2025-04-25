"""
/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */
"""
import zipfile
import os

def comprimir_archivo(ruta_origen, ruta_destino_zip):
    with zipfile.ZipFile(ruta_destino_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(ruta_origen):
            zipf.write(ruta_origen, arcname=os.path.basename(ruta_origen))
            print(f"Archivo comprimido: {ruta_destino_zip}")
        elif os.path.isdir(ruta_origen):
            for root, dirs, files in os.walk(ruta_origen):
                for file in files:
                    ruta_completa = os.path.join(root, file)
                    arcname = os.path.relpath(ruta_completa, start=ruta_origen)
                    zipf.write(ruta_completa, arcname=arcname)
            print(f"Carpeta comprimida: {ruta_destino_zip}")
        else:
            print("Ruta no válida.")

# Ejemplo de uso
origen = "camiseta.txt"  # O una carpeta, por ejemplo: "mi_carpeta/"
destino = "camiseta.zip"
comprimir_archivo(origen, destino)
