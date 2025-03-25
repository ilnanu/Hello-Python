# Desarrolla un programa capaz de crear un archivo XML que guarde los siguientes datos (sintaxis correcta en cada caso):
# Nombre, Edad, Fecha de nacimiento, Listado de lenguajes de programación
# Muestra el contenido del archivo
# Borra el archivo

# Adicionalmente, utilizando la lógica del archivo anterior, crea un programa capaz de leer y transformar en una misma clase custom los datos alamecenados en el XML.

import xml.etree.ElementTree as ET

def crear_xml(data):
    # Crear el elemento raíz
    root = ET.Element('Persona')

    # Añadir subelementos
    ET.SubElement(root, 'Nombre').text = data['Nombre']
    ET.SubElement(root, 'Edad').text = data['Edad']
    ET.SubElement(root, 'Fecha_de_nacimiento').text = data['Fecha_de_nacimiento']

    lenguajes = ET.SubElement(root, 'Lenguajes_de_programacion')
    for lenguaje in data['Lenguajes_de_programacion']:
        ET.SubElement(lenguajes, 'Lenguaje').text = lenguaje

    # Crear el árbol y guardar en un archivo
    tree = ET.ElementTree(root)
    with open('persona.xml', 'wb') as file:
        tree.write(file)

def mostrar_contenido():
    with open('persona.xml', 'r') as file:
        contenido = file.read()
    return contenido

def borrar_archivo():
    import os
    if os.path.exists('persona.xml'):
        os.remove('persona.xml')
        return 'Archivo eliminado correctamente.'
    else:
        return 'El archivo no existe.'

# Datos a guardar
data = {
    'Nombre': 'Juan Pérez',
    'Edad': '30',
    'Fecha_de_nacimiento': '1995-05-15',
    'Lenguajes_de_programacion': ['Python', 'Java', 'C++']
}

# Crear archivo XML
crear_xml(data)

# Mostrar contenido
print("Contenido del archivo:")
print(mostrar_contenido())

# Borrar archivo
print("\nResultado al borrar el archivo:")
print(borrar_archivo())

import xml.etree.ElementTree as ET

class Persona:
    def __init__(self, nombre, edad, fecha_de_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.lenguajes = lenguajes

    def __repr__(self):
        return f"Persona(Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Lenguajes: {self.lenguajes})"

def leer_xml_y_transformar():
    # Crear nuevamente el archivo XML para leerlo
    data = {
        'Nombre': 'Juan Pérez',
        'Edad': '30',
        'Fecha_de_nacimiento': '1995-05-15',
        'Lenguajes_de_programacion': ['Python', 'Java', 'C++']
    }

    root = ET.Element('Persona')
    ET.SubElement(root, 'Nombre').text = data['Nombre']
    ET.SubElement(root, 'Edad').text = data['Edad']
    ET.SubElement(root, 'Fecha_de_nacimiento').text = data['Fecha_de_nacimiento']

    lenguajes = ET.SubElement(root, 'Lenguajes_de_programacion')
    for lenguaje in data['Lenguajes_de_programacion']:
        ET.SubElement(lenguajes, 'Lenguaje').text = lenguaje

    tree = ET.ElementTree(root)
    with open('persona.xml', 'wb') as file:
        tree.write(file)

    # Leer el archivo XML
    tree = ET.parse('persona.xml')
    root = tree.getroot()

    # Extraer datos
    nombre = root.find('Nombre').text
    edad = root.find('Edad').text
    fecha_de_nacimiento = root.find('Fecha_de_nacimiento').text
    lenguajes = [lenguaje.text for lenguaje in root.find('Lenguajes_de_programacion')]

    # Transformar en una clase custom
    persona = Persona(nombre, edad, fecha_de_nacimiento, lenguajes)

    # Borrar el archivo después de leerlo
    import os
    if os.path.exists('persona.xml'):
        os.remove('persona.xml')

    return persona

# Leer y transformar datos
print("\nDatos transformados en clase custom:")
print(leer_xml_y_transformar())
