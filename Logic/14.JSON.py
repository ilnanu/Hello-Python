# Desarrolla un programa capaz de crear un archivo JSON que guarde los siguientes datos (sintaxis correcta en cada caso):
# Nombre, Edad, Fecha de nacimiento, Listado de lenguajes de programación
# Muestra el contenido del archivo
# Borra el archivo

# Adicionalmente, utilizando la lógica del archivo anterior, crea un programa capaz de leer y transformar en una misma clase custom los datos alamecenados en el XML.
import json

def crear_json(data):
    # Crear archivo JSON
    with open('persona.json', 'w') as file:
        json.dump(data, file, indent=4)

def mostrar_contenido():
    with open('persona.json', 'r') as file:
        contenido = file.read()
    return contenido

def borrar_archivo():
    import os
    if os.path.exists('persona.json'):
        os.remove('persona.json')
        return 'Archivo eliminado correctamente.'
    else:
        return 'El archivo no existe.'

# Datos a guardar
data = {
    'Nombre': 'Juan Pérez',
    'Edad': 30,
    'Fecha_de_nacimiento': '1995-05-15',
    'Lenguajes_de_programacion': ['Python', 'Java', 'C++']
}

# Crear archivo JSON
crear_json(data)

# Mostrar contenido
print("Contenido del archivo:")
print(mostrar_contenido())

# Borrar archivo
print("\nResultado al borrar el archivo:")
print(borrar_archivo())

import json

class Persona:
    def __init__(self, nombre, edad, fecha_de_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.lenguajes = lenguajes

    def __repr__(self):
        return f"Persona(Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Lenguajes: {self.lenguajes})"

def leer_json_y_transformar():
    # Crear nuevamente el archivo JSON para leerlo
    data = {
        'Nombre': 'Juan Pérez',
        'Edad': 30,
        'Fecha_de_nacimiento': '1995-05-15',
        'Lenguajes_de_programacion': ['Python', 'Java', 'C++']
    }

    with open('persona.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Leer el archivo JSON
    with open('persona.json', 'r') as file:
        datos_json = json.load(file)

    # Transformar en una clase custom
    persona = Persona(
        datos_json['Nombre'],
        datos_json['Edad'],
        datos_json['Fecha_de_nacimiento'],
        datos_json['Lenguajes_de_programacion']
    )

    # Borrar el archivo después de leerlo
    import os
    if os.path.exists('persona.json'):
        os.remove('persona.json')

    return persona

# Leer y transformar datos
print("\nDatos transformados en clase custom:")
print(leer_json_y_transformar())
