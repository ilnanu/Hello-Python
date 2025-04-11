"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""
class SesionUsuario:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(SesionUsuario, cls).__new__(cls)
            cls._instancia.usuario = None
        return cls._instancia

    def asignar_usuario(self, id, username, nombre, email):
        self.usuario = {
            "id": id,
            "username": username,
            "nombre": nombre,
            "email": email
        }
        print(f"✅ Usuario asignado: {self.usuario['username']}")

    def obtener_usuario(self):
        if self.usuario:
            return self.usuario
        else:
            print("⚠️ No hay usuario en sesión.")
            return None

    def cerrar_sesion(self):
        if self.usuario:
            print(f"🔒 Sesión cerrada para: {self.usuario['username']}")
            self.usuario = None
        else:
            print("⚠️ No hay sesión activa para cerrar.")


# Ejemplo de uso
if __name__ == "__main__":
    sesion1 = SesionUsuario()
    sesion1.asignar_usuario(1, "jdoe", "John Doe", "jdoe@example.com")

    sesion2 = SesionUsuario()
    print("\n📋 Datos de usuario desde otra instancia:")
    print(sesion2.obtener_usuario())

    print("\n🧪 Verificando que ambas instancias son la misma:")
    print(sesion1 is sesion2)  # Debe ser True

    sesion2.cerrar_sesion()
    print(sesion1.obtener_usuario())

