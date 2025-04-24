"""
/*
 * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta 
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
 */
 Obtener token de autenticación:
 curl -X POST "https://id.twitch.tv/oauth2/token" \
-d "client_id=TU_CLIENT_ID" \
-d "client_secret=TU_CLIENT_SECRET" \
-d "grant_type=client_credentials"
 """
import requests
import time

# Sustituye con tus credenciales de Twitch
CLIENT_ID = "TU_CLIENT_ID"
AUTH_TOKEN = "TU_AUTH_TOKEN"

HEADERS = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

# Lista de participantes desde el tweet (puedes adaptarla a mano o scrapear el tweet)
PARTICIPANTES = [
    "Rubiu5", "Auronplay", "Ibai", "TheGrefg", "xQc", "ElMariana", "Rivers_gg", "JuanSGuarnizo",
    "BarbeQ", "Biyin_", "Cristinini", "Folagor03", "Gemita", "Illojuan", "Komanche",
    "Luzu", "Quackity", "Reborn_Live", "Spursito", "Zeling", "Sekiam", "Mayichi", "Axel", "Tortillaland", "Karchez"
]

def obtener_usuario(usuario):
    url = f"https://api.twitch.tv/helix/users?login={usuario}"
    resp = requests.get(url, headers=HEADERS)
    data = resp.json()
    if data["data"]:
        return data["data"][0]
    return None

def obtener_seguidores(user_id):
    url = f"https://api.twitch.tv/helix/users/follows?to_id={user_id}"
    resp = requests.get(url, headers=HEADERS)
    data = resp.json()
    return data.get("total", 0)

datos_usuarios = []

for nombre in PARTICIPANTES:
    print(f"Buscando datos de: {nombre}")
    user = obtener_usuario(nombre)
    if user:
        seguidores = obtener_seguidores(user["id"])
        datos_usuarios.append({
            "nombre": nombre,
            "seguidores": seguidores,
            "creacion": user["created_at"]
        })
    else:
        datos_usuarios.append({
            "nombre": nombre,
            "seguidores": None,
            "creacion": None
        })
    time.sleep(0.5)  # Para evitar rate limiting

# Ranking por seguidores
ranking_seguidores = sorted(
    [u for u in datos_usuarios if u["seguidores"] is not None],
    key=lambda x: x["seguidores"],
    reverse=True
)

# Ranking por antigüedad
ranking_antiguedad = sorted(
    [u for u in datos_usuarios if u["creacion"] is not None],
    key=lambda x: x["creacion"]
)

print("\n📊 Ranking por número de seguidores:")
for i, u in enumerate(ranking_seguidores, 1):
    print(f"{i}. {u['nombre']} - {u['seguidores']} seguidores")

print("\n📜 Ranking por antigüedad:")
for i, u in enumerate(ranking_antiguedad, 1):
    print(f"{i}. {u['nombre']} - Creado el {u['creacion']}")

print("\n❌ Usuarios no encontrados en Twitch:")
no_encontrados = [u for u in datos_usuarios if u["seguidores"] is None]
for u in no_encontrados:
    print(f"- {u['nombre']}")
