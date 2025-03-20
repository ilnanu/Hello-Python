# Implementa la jerarquia de una empresa de desarrollo formada por Empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su actividad, y almacenan los empleados a su cargo

class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}")


class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def mostrar_empleados_a_cargo(self):
        print(f"Empleados a cargo de {self.nombre}:")
        for empleado in self.empleados_a_cargo:
            empleado.mostrar_informacion()


class GerenteDeProyectos(Gerente):
    def __init__(self, id, nombre, proyecto):
        super().__init__(id, nombre)
        self.proyecto = proyecto

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Proyecto: {self.proyecto}")


class Programador(Empleado):
    def __init__(self, id, nombre, lenguaje):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje de programación: {self.lenguaje}")


# Ejemplo de uso
gerente = Gerente(1, "Carlos")
programador1 = Programador(2, "Ana", "Python")
programador2 = Programador(3, "Luis", "JavaScript")

gerente.agregar_empleado(programador1)
gerente.agregar_empleado(programador2)

gerente.mostrar_informacion()
gerente.mostrar_empleados_a_cargo()

gerente_proyectos = GerenteDeProyectos(4, "Marta", "Proyecto X")
gerente_proyectos.agregar_empleado(gerente)
gerente_proyectos.mostrar_informacion()
gerente_proyectos.mostrar_empleados_a_cargo()
