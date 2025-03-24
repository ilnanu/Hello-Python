import os

ARCHIVO = 'ventas.txt'

def cargar_ventas():
    try:
        with open(ARCHIVO, 'r') as f:
            ventas = []
            for linea in f:
                nombre, cantidad, precio = linea.strip().split(',')
                ventas.append({
                    'nombre': nombre.strip(),
                    'cantidad': int(cantidad),
                    'precio': float(precio)
                })
            return ventas
    except FileNotFoundError:
        return []

def guardar_ventas(ventas):
    with open(ARCHIVO, 'w') as f:
        for p in ventas:
            f.write(f"{p['nombre']}, {p['cantidad']}, {p['precio']}\n")

def mostrar_menu():
    print('\n===== GESTIÓN DE VENTAS =====')
    print('1. Añadir producto')
    print('2. Consultar productos')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Total ventas')
    print('6. Ventas por producto')
    print('7. Salir')

def añadir_producto(ventas):
    nombre = input('Nombre del producto: ')
    cantidad = int(input('Cantidad vendida: '))
    precio = float(input('Precio unitario: '))
    ventas.append({
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    })
    guardar_ventas(ventas)
    print('Producto añadido!')

def listar_productos(ventas):
    print('\n=== LISTADO DE PRODUCTOS ===')
    for i, p in enumerate(ventas):
        print(f"{i+1}. {p['nombre']} - {p['cantidad']} u. - ${p['precio']} c/u")

def actualizar_producto(ventas):
    listar_productos(ventas)
    indice = int(input('Índice del producto a actualizar: ')) - 1
    if 0 <= indice < len(ventas):
        p = ventas[indice]
        p['cantidad'] = int(input(f"Nueva cantidad ({p['cantidad']}): ") or p['cantidad'])
        p['precio'] = float(input(f"Nuevo precio ({p['precio']}): ") or p['precio'])
        guardar_ventas(ventas)
        print('Producto actualizado!')
    else:
        print('Índice inválido.')

def eliminar_producto(ventas):
    listar_productos(ventas)
    indice = int(input('Índice del producto a eliminar: ')) - 1
    if 0 <= indice < len(ventas):
        del ventas[indice]
        guardar_ventas(ventas)
        print('Producto eliminado!')
    else:
        print('Índice inválido.')

def calcular_total(ventas):
    total = sum(p['cantidad'] * p['precio'] for p in ventas)
    print(f"\nTOTAL VENDIDO: ${total:.2f}")

def ventas_por_producto(ventas):
    nombre = input('Nombre del producto: ')
    total = sum(p['cantidad'] * p['precio'] for p in ventas if p['nombre'].lower() == nombre.lower())
    print(f"TOTAL PARA {nombre}: ${total:.2f}")

def salir(ventas):
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    print('\nArchivo borrado. ¡Hasta luego!')
    exit()

def main():
    ventas = cargar_ventas()
    while True:
        mostrar_menu()
        opcion = input('Seleccione opción: ')

        if opcion == '1':
            añadir_producto(ventas)
        elif opcion == '2':
            listar_productos(ventas)
        elif opcion == '3':
            actualizar_producto(ventas)
        elif opcion == '4':
            eliminar_producto(ventas)
        elif opcion == '5':
            calcular_total(ventas)
        elif opcion == '6':
            ventas_por_producto(ventas)
        elif opcion == '7':
            salir(ventas)
        else:
            print('Opción inválida!')

if __name__ == "__main__":
    main()
