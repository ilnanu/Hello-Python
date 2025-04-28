# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

"""
1. Crea una variable con la fecha y hora actual.
2. Imprime solo el año, mes y día de la fecha actual.
3. Crea una fecha específica: 25 de diciembre de 2025 y
muéstrala.
4. Muestra solo la hora, los minutos y los segundos de un
objeto time.
5. Calcula cuántos días faltan para el 1 de enero del año
siguiente.
6. Crea una función que reciba una fecha y devuelva su
timestamp.
7. Suma 30 días a la fecha actual usando timedelta.
8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30
días como simplificación).
9. Compara dos fechas y muestra cuál es anterior.
10. Crea una lista con varias fechas y ordénalas
cronológicamente
"""
# Ejercicio 1: Crear una variable con la fecha y hora actual
current_datetime = datetime.now()
print("Fecha y hora actual:", current_datetime)

# Ejercicio 2: Imprimir solo el año, mes y día de la fecha actual
date_today = current_datetime.date()
print("Año:", date_today.year)
print("Mes:", date_today.month)
print("Día:", date_today.day)

# Ejercicio 3: Crear una fecha específica: 25 de diciembre de 2025
specific_date = date(2025, 12, 25)
print("Fecha específica:", specific_date)

# Ejercicio 4: Mostrar solo la hora, los minutos y los segundos de un objeto time
define_time = time(15, 30, 45)  # 3:30:45 PM
print("Hora:", define_time.hour)    
print("Minutos:", define_time.minute)
print("Segundos:", define_time.second)

# Ejercicio 5: Calcular cuántos días faltan para el 1 de enero del año siguiente
next_year = date_today.year + 1
next_year_date = date(next_year, 1, 1)
days_until_next_year = (next_year_date - date_today).days
print("Días hasta el 1 de enero del año siguiente:", days_until_next_year)

# Ejercicio 6: Crear una función que reciba una fecha y devuelva su timestamp
def get_timestamp(date_obj):
    # Convertimos el objeto date a datetime para obtener el timestamp
    datetime_obj = datetime.combine(date_obj, datetime.min.time())
    return datetime_obj.timestamp()
date_obj = date(2023, 10, 6)
timestamp = get_timestamp(date_obj) 
print("Timestamp de la fecha", date_obj, ":", timestamp)

# Ejercicio 7: Sumar 30 días a la fecha actual usando timedelta
date_plus_30_days = current_datetime + timedelta(days=30)
print("Fecha actual + 30 días:", date_plus_30_days) 

# Ejercicio 8: Crear una fecha y añadir 1 mes (simplificación sumando 30 días)
date_plus_1_month = current_datetime + timedelta(days=30)
print("Fecha actual + 1 mes (30 días):", date_plus_1_month)

# Ejercicio 9: Comparar dos fechas y mostrar cuál es anterior
date1 = date(2023, 10, 6)
date2 = date(2024, 1, 1)
if date1 < date2:
    print(f"La fecha {date1} es anterior a {date2}.")
elif date1 > date2:
    print(f"La fecha {date1} es posterior a {date2}.")
else:
    print(f"Las fechas {date1} y {date2} son iguales.")

# Ejercicio 10: Crear una lista con varias fechas y ordenarlas cronológicamente
list_of_dates = [
    date(2023, 10, 6),
    date(2022, 5, 15),
    date(2024, 1, 1),
    date(2023, 7, 20)
]
sorted_dates = sorted(list_of_dates)
print("Fechas ordenadas cronológicamente:")
for d in sorted_dates:
    print(d)

# Fin del ejercicio







