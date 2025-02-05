# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

def write_file(file_name, data):
    with open(file_name, "w") as file:
        file.write(data)

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()
    
