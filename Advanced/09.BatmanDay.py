"""
/*
 * EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas. 
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los 
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones: 
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el 
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */
"""
import datetime
import calendar

def obtener_batman_day(anio):
    # Buscar el tercer sábado de septiembre
    mes = 9  # septiembre
    sabados = [day for day in range(1, 31) 
               if calendar.weekday(anio, mes, day) == 5]  # 5: sábado
    return datetime.date(anio, mes, sabados[2])  # tercer sábado

print("🦇 Próximos Batman Day hasta el centenario:")
for anio in range(2024, 2040):  # De 85 a 100 aniversario
    dia = obtener_batman_day(anio)
    print(f"{anio} ({anio - 1939}º aniversario): {dia.strftime('%A, %d %B %Y')}")

import random

TAMANO = 20
UMBRAL_AMENAZA = 20

# Simular sensores: lista de (x, y, amenaza)
def generar_sensores(num_sensores):
    sensores = []
    for _ in range(num_sensores):
        x = random.randint(0, TAMANO - 1)
        y = random.randint(0, TAMANO - 1)
        amenaza = random.randint(0, 10)
        sensores.append((x, y, amenaza))
    return sensores

# Crear mapa de Gotham
def construir_mapa(sensores):
    mapa = [[0 for _ in range(TAMANO)] for _ in range(TAMANO)]
    for x, y, amenaza in sensores:
        mapa[x][y] = amenaza
    return mapa

# Buscar la mejor zona 3x3
def buscar_zona_critica(mapa):
    max_amenaza = -1
    centro_critico = None
    for i in range(TAMANO - 2):
        for j in range(TAMANO - 2):
            suma = sum(mapa[i + dx][j + dy] for dx in range(3) for dy in range(3))
            if suma > max_amenaza:
                max_amenaza = suma
                centro_critico = (i + 1, j + 1)
    return centro_critico, max_amenaza

# Calcular distancia Manhattan
def distancia_batcueva(centro):
    x, y = centro
    return abs(x - 0) + abs(y - 0)

# Programa principal
if __name__ == "__main__":
    sensores = generar_sensores(100)
    mapa = construir_mapa(sensores)
    centro, amenaza_total = buscar_zona_critica(mapa)
    distancia = distancia_batcueva(centro)
    activar_protocolo = amenaza_total > UMBRAL_AMENAZA

    print("\n🛡️ Sistema de Seguridad de la Batcueva:")
    print(f"📍 Centro zona crítica: {centro}")
    print(f"🔥 Nivel total de amenaza: {amenaza_total}")
    print(f"📏 Distancia a la Batcueva (0,0): {distancia}")
    print(f"{'🚨 PROTOCOLO ACTIVADO' if activar_protocolo else '✅ Sin amenazas graves'}")
