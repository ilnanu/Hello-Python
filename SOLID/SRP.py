"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
#/Ejemplo erroneo
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar_usuario(self):
        # Código para guardar el usuario en la base de datos
        pass

    def enviar_email(self):
        # Código para enviar un email al usuario
        pass
# Ejemplo OK
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
class UsuarioDB:
    def guardar_usuario(self, usuario):
        # Código para guardar el usuario en la base de datos
        pass
class EmailService:
    def enviar_email(self, usuario):
        # Código para enviar un email al usuario
        pass
# Ejemplo de uso
usuario = Usuario("Alice", "alice@example.com")
gestor = UsuarioDB()
email_service = EmailService()

gestor.guardar_usuario(usuario)
email_service.enviar_email(usuario)

"""
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
"""

# ❌ Ejemplo que VIOLA el SRP
class Library:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, titulo, autor, copias):
        self.libros.append({"titulo": titulo, "autor": autor, "copias": copias})

    def registrar_usuario(self, nombre, id_usuario, email):
        self.usuarios.append({"nombre": nombre, "id": id_usuario, "email": email})

    def prestar_libro(self, id_usuario, titulo_libro):
        libro = next((l for l in self.libros if l["titulo"] == titulo_libro and l["copias"] > 0), None)
        if libro:
            self.prestamos.append({"usuario": id_usuario, "libro": titulo_libro})
            libro["copias"] -= 1
            print(f"Libro '{titulo_libro}' prestado a usuario {id_usuario}")
        else:
            print("Libro no disponible")

    def devolver_libro(self, id_usuario, titulo_libro):
        prestamo = next((p for p in self.prestamos if p["usuario"] == id_usuario and p["libro"] == titulo_libro), None)
        if prestamo:
            self.prestamos.remove(prestamo)
            for libro in self.libros:
                if libro["titulo"] == titulo_libro:
                    libro["copias"] += 1
                    break
            print(f"Libro '{titulo_libro}' devuelto por usuario {id_usuario}")
        else:
            print("No se encontró el préstamo")


# ✅ Refactorizado aplicando SRP
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

class Usuario:
    def __init__(self, nombre, id_usuario, email):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email

class GestorLibros:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, titulo, autor, copias):
        self.libros.append(Libro(titulo, autor, copias))

    def buscar_libro(self, titulo):
        return next((libro for libro in self.libros if libro.titulo == titulo), None)

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, id_usuario, email):
        self.usuarios.append(Usuario(nombre, id_usuario, email))

    def obtener_usuario(self, id_usuario):
        return next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

class GestorPrestamos:
    def __init__(self, gestor_libros, gestor_usuarios):
        self.prestamos = []
        self.gestor_libros = gestor_libros
        self.gestor_usuarios = gestor_usuarios

    def prestar_libro(self, id_usuario, titulo_libro):
        libro = self.gestor_libros.buscar_libro(titulo_libro)
        usuario = self.gestor_usuarios.obtener_usuario(id_usuario)
        if libro and usuario and libro.copias > 0:
            self.prestamos.append({"usuario": id_usuario, "libro": titulo_libro})
            libro.copias -= 1
            print(f"✅ '{titulo_libro}' prestado a {usuario.nombre}")
        else:
            print("❌ Libro no disponible o usuario no encontrado")

    def devolver_libro(self, id_usuario, titulo_libro):
        prestamo = next((p for p in self.prestamos if p["usuario"] == id_usuario and p["libro"] == titulo_libro), None)
        if prestamo:
            self.prestamos.remove(prestamo)
            libro = self.gestor_libros.buscar_libro(titulo_libro)
            if libro:
                libro.copias += 1
            print(f"🔄 '{titulo_libro}' devuelto por usuario {id_usuario}")
        else:
            print("⚠️ Préstamo no encontrado")

# 🧪 Ejemplo de uso
if __name__ == '__main__':
    libros = GestorLibros()
    usuarios = GestorUsuarios()
    prestamos = GestorPrestamos(libros, usuarios)

    libros.registrar_libro("1984", "George Orwell", 2)
    usuarios.registrar_usuario("Alice", 1, "alice@mail.com")

    prestamos.prestar_libro(1, "1984")
    prestamos.devolver_libro(1, "1984")
