# Este es un ejemplo de una agenda simple, donde se pueden añadir, modificar, buscar y eliminar contactos.

def mi_agenda():

    agenda = {}     # Esta es la agenda como tal
    def up_numero():        # Esta es la funcion para añadir/modificar un contacto
        numero = input("Introduce numero de contacto:")
        if numero.isdigit() and len(numero) > 0 and len(numero) <= 10:
            agenda[name] = numero
            print("Contacto añadido.")
        else:
            print("Solo se aceptan numeros de hasta 10 digitos.")
    
    while True:     # De esta manera se mantiene la funcion en bucle

        # Se inicia imprimiendo el menu

        print("")
        print("1 - Buscar contacto")
        print("2 - Agregar Contacto")
        print("3 - Actualizar contacto")
        print("4 - Eliminar contactos")
        print("5 - Salir")
        print("6 - Ver agenda")

        option = input("Elige la opcion deseada:")      # Input se utiliza para poder interactuar con terminal

        match option:       # Se puede usar if, elif y else, pero en python existe match
            case "1":
                name = input("Introduce el nombre de contacto:")
                if name in agenda:
                    print(
                        f"El numero de {name} es {agenda[name]}")
                else:
                    print(f"El nombre {name} no existe en la agenda.")
            case "2":
                name = input("Introduce nombre de contacto:")
                up_numero()
            case "3":
                name = input("Introduce el nombre de contacto que desea actualizar:")
                if name in agenda:
                    up_numero()
                else:
                    print(f"El nombre {name} no existe en la agenda.")

            case "4":
                name = input("Introduce el nombre de contacto que desea eliminar:")
                if name in agenda:
                    del agenda[name]
                    print("El contacto se ha borrado.")
                else:
                    print(f"El nombre {name} no existe en la agenda.")
            case "5":
                print("Saliendo")
                break
            case "6":
                    print(agenda)
            case _:
                print("Opcion invalida. Elige del 1 al 6")


mi_agenda()

