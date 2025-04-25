"""
/*
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario selecciona qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
 */
"""
class CalendarioADEViento:
    def __init__(self):
        self.dias_descubiertos = set()  # Conjunto de días descubiertos

    def dibujar_calendario(self):
        dia = 1
        calendario = ''
        
        # Recorremos las filas del calendario (6 filas de 4 días)
        for i in range(6):
            fila = ''
            for j in range(4):
                # Si el día ha sido descubierto, mostramos asteriscos
                # Si no, mostramos el número del día
                if dia in self.dias_descubiertos:
                    fila += '**** '
                else:
                    fila += f'*{self.formatear_dia(dia)}* '
                dia += 1
                if dia > 24:
                    break
            calendario += fila.strip() + '\n'
        
        print(calendario)

    def formatear_dia(self, dia):
        """ Formatea el día para que siempre tenga dos dígitos """
        return f'{dia:02d}'

    def seleccionar_dia(self, dia):
        """ Permite al usuario seleccionar un día para descubrirlo """
        if dia in self.dias_descubiertos:
            print(f'El día {self.formatear_dia(dia)} ya ha sido descubierto.')
        else:
            self.dias_descubiertos.add(dia)
            print(f'¡Felicidades! Has descubierto el día {self.formatear_dia(dia)}.')
        self.dibujar_calendario()  # Redibuja el calendario actualizado

# Crear el calendario
calendario = CalendarioADEViento()

# Dibujar el calendario inicial
calendario.dibujar_calendario()

# Simulación de selección de días
calendario.seleccionar_dia(1)  # Seleccionar el día 1
calendario.seleccionar_dia(1)  # Intentar seleccionar el día 1 de nuevo
calendario.seleccionar_dia(5)  # Seleccionar el día 5
