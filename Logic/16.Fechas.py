from datetime import datetime

"""
Ejercicio
"""

now = datetime.now()
birth_date = datetime(1987, 4, 29, 12, 0, 0)

print(now)
print(birth_date)

difference = now - birth_date
print(type(difference))

print(f"Tengo {difference.days // 365} aÃ±os.")

"""
Extra
"""

# DÃ­a, mes y aÃ±o
print(birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("%d/%m/%Y"))

# Horas, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))

# DÃ­a del aÃ±o
print(birth_date.strftime("%j"))

# DÃ­a de la semana
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%h"))
print(birth_date.strftime("%B"))

# RepresentaciÃ³n por defecto del locale
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%p"))
