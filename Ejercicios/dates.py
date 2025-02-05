# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas.

import datetime

def current_date():
    return datetime.date.today()

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

