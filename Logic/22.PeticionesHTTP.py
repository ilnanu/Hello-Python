"""
Utilizando un mecanismo de peticiones HTTP de python, 
realiza una petición a la web que tu quieras, 
verifica que dicha petición fue exitosa y muestra por consola el contenido de la web.
"""
import requests

# URL de ejemplo
url = "https://www.example.com"

try:
    response = requests.get(url)

    # Verificamos si la respuesta fue exitosa (código 200)
    if response.status_code == 200:
        print("✅ Petición exitosa")
        print("Contenido de la página:")
        print(response.text)
    else:
        print(f"❌ La petición falló con código de estado: {response.status_code}")

except requests.RequestException as e:
    print(f"⚠️ Error durante la petición HTTP: {e}")

"""
Utilizando la PokéAPI (https://pokeapi.co), crea un programa por terminal al que le puedas solicitar
información de un Pokémon concreto utilizando su nombre o número.
- Muestra el nombre, id, peso, altura y tipo(s) del Pokémon.
- Si el Pokémon no existe, muestra un mensaje de error.
- Muestra el nombre de su cadena de evoluciones.
- Muestra los juegos en los que aparece.
- Controla posibles errores.
"""
#import requests

def obtener_pokemon(nombre_o_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id.lower()}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code != 200:
            print("\n❌ Pokémon no encontrado.")
            return

        datos = respuesta.json()

        nombre = datos['name']
        id_pokemon = datos['id']
        peso = datos['weight']
        altura = datos['height']
        tipos = [tipo['type']['name'] for tipo in datos['types']]

        print(f"\n🧾 Información de {nombre.capitalize()}")
        print(f"ID: {id_pokemon}")
        print(f"Peso: {peso}")
        print(f"Altura: {altura}")
        print(f"Tipo(s): {', '.join(tipos)}")

        # Mostrar juegos donde aparece
        juegos = {entry['version']['name'] for entry in datos['game_indices']}
        print(f"\n🎮 Aparece en los juegos:")
        for juego in sorted(juegos):
            print(f"- {juego}")

        # Obtener cadena de evolución
        url_especie = datos['species']['url']
        especie = requests.get(url_especie).json()
        url_evoluciones = especie['evolution_chain']['url']
        cadena = requests.get(url_evoluciones).json()

        print("\n🔗 Cadena de evoluciones:")
        mostrar_cadena(cadena['chain'])

    except requests.RequestException as e:
        print(f"\n⚠️ Error de conexión: {e}")

def mostrar_cadena(cadena):
    actual = cadena['species']['name']
    print(f"- {actual}")
    for evolucion in cadena['evolves_to']:
        mostrar_cadena(evolucion)

if __name__ == "__main__":
    nombre = input("Introduce el nombre o número del Pokémon: ")
    obtener_pokemon(nombre)

