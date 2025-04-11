"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo a registrar
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Ejemplos por nivel
logging.debug("Este es un mensaje DEBUG: útil para desarrollo.")
logging.info("Este es un mensaje INFO: todo funciona correctamente.")
logging.warning("Este es un WARNING: algo inesperado ha ocurrido.")
logging.error("Este es un ERROR: algo ha fallado.")
logging.critical("Este es un CRITICAL: fallo crítico del sistema.")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
"""
import logging
import time

# Configuración del logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Lista de tareas
tareas = []

# Función para añadir tarea
def añadir_tarea(nombre, descripcion):
    start_time = time.time()  # Empezamos a medir el tiempo de ejecución
    tareas.append({'nombre': nombre, 'descripcion': descripcion})
    end_time = time.time()  # Fin de la medición del tiempo
    execution_time = end_time - start_time
    logging.info(f'✔️ Tarea añadida: {nombre}')
    logging.debug(f'⏱ Tiempo de ejecución de añadir_tarea: {execution_time:.4f} segundos')

# Función para eliminar tarea
def eliminar_tarea(nombre):
    start_time = time.time()
    tarea_encontrada = False
    for tarea in tareas:
        if tarea['nombre'] == nombre:
            tareas.remove(tarea)
            tarea_encontrada = True
            break
    end_time = time.time()
    execution_time = end_time - start_time
    if tarea_encontrada:
        logging.info(f'✔️ Tarea eliminada: {nombre}')
    else:
        logging.warning(f'⚠️ Tarea no encontrada: {nombre}')
    logging.debug(f'⏱ Tiempo de ejecución de eliminar_tarea: {execution_time:.4f} segundos')

# Función para listar tareas
def listar_tareas():
    logging.info('📋 Listando tareas actuales:')
    if tareas:
        for tarea in tareas:
            logging.info(f'📝 {tarea["nombre"]}: {tarea["descripcion"]}')
    else:
        logging.warning('⚠️ No hay tareas en la lista.')

# Ejemplo de uso
if __name__ == '__main__':
    añadir_tarea('Comprar leche', 'Ir al supermercado y comprar leche.')
    añadir_tarea('Estudiar Python', 'Practicar programación en Python para mejorar habilidades.')
    listar_tareas()
    eliminar_tarea('Comprar leche')
    listar_tareas()
