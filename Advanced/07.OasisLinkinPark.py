"""
 * EJERCICIO:
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
"""
import requests
import base64

# Rellena con tus credenciales de Spotify
CLIENT_ID = "TU_CLIENT_ID"
CLIENT_SECRET = "TU_CLIENT_SECRET"

# Obtener token de autenticación
def obtener_token():
    auth = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    headers = {
        "Authorization": f"Basic {auth_base64}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json()["access_token"]

# Buscar artista por nombre
def buscar_artista(nombre, token):
    url = f"https://api.spotify.com/v1/search?q={nombre}&type=artist"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    items = response.json()["artists"]["items"]
    return items[0] if items else None

# Obtener top tracks de un artista
def obtener_top_tracks(artist_id, token, market="US"):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()["tracks"]

# Comparar artistas
def comparar_artistas(artista1, artista2):
    token = obtener_token()

    datos = {}
    for nombre in [artista1, artista2]:
        artista = buscar_artista(nombre, token)
        top_tracks = obtener_top_tracks(artista["id"], token)
        datos[nombre] = {
            "followers": artista["followers"]["total"],
            "popularity": artista["popularity"],
            "top_track": top_tracks[0]["name"],
            "top_track_popularity": top_tracks[0]["popularity"]
        }

    print("\n🎵 RESULTADOS COMPARATIVOS:")
    for nombre in datos:
        info = datos[nombre]
        print(f"\n🎤 {nombre}")
        print(f"- Seguidores: {info['followers']:,}")
        print(f"- Popularidad (0-100): {info['popularity']}")
        print(f"- Canción más popular: {info['top_track']} (popularidad: {info['top_track_popularity']})")

    # Evaluar popularidad
    print("\n🔥 VEREDICTO FINAL:")
    puntos = {artista1: 0, artista2: 0}

    # Comparación por puntos
    for criterio in ["followers", "popularity", "top_track_popularity"]:
        ganador = artista1 if datos[artista1][criterio] > datos[artista2][criterio] else artista2
        puntos[ganador] += 1

    if puntos[artista1] > puntos[artista2]:
        print(f"🏆 ¡{artista1} es más popular!")
    elif puntos[artista1] < puntos[artista2]:
        print(f"🏆 ¡{artista2} es más popular!")
    else:
        print("🤝 ¡Empate técnico!")

# Ejecutar comparación
if __name__ == "__main__":
    comparar_artistas("Oasis", "Linkin Park")
