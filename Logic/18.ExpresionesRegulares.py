"""
Crea 3 expresiones regulares (a tu criterio) capaces de:
* Validar un email
* Validar un número de teléfono
* Validar una url
"""
import re

# Expresiones regulares
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?\d{1,4}[\s-]?\d{1,14}([\s-]?\d{1,13})?$'
URL_REGEX = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}([\/\w.-]*)*\/?$'

def validar_dato(tipo: str, dato: str):
    regex = {
        "email": EMAIL_REGEX,
        "telefono": PHONE_REGEX,
        "url": URL_REGEX
    }.get(tipo)
    
    if regex and re.match(regex, dato):
        print(f"{tipo.capitalize()} válido: {dato}")
    else:
        print(f"{tipo.capitalize()} inválido: {dato}")

def main():
    # Validaciones
    validar_dato("email", "usuario@example.com")
    validar_dato("telefono", "+34 600-123-456")
    validar_dato("url", "https://www.ejemplo.com")

main()

