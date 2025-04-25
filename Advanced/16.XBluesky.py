"""
/*
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
 */
"""
import uuid
from datetime import datetime

class Usuario:
    def __init__(self, nombre):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.seguidores = set()
        self.seguidos = set()
        self.posts = []
    
    def seguir(self, otro_usuario):
        if otro_usuario != self:
            self.seguidos.add(otro_usuario)
            otro_usuario.seguidores.add(self)
        else:
            print("No puedes seguirte a ti mismo.")
    
    def dejar_de_seguir(self, otro_usuario):
        if otro_usuario != self:
            self.seguidos.discard(otro_usuario)
            otro_usuario.seguidores.discard(self)
        else:
            print("No puedes dejar de seguirte a ti mismo.")
    
    def crear_post(self, texto):
        if len(texto) > 200:
            print("El texto excede el límite de 200 caracteres.")
            return
        post = Post(self, texto)
        self.posts.append(post)
        print(f"Post creado con ID: {post.id}")
    
    def eliminar_post(self, post_id):
        post = next((p for p in self.posts if p.id == post_id), None)
        if post:
            self.posts.remove(post)
            print(f"Post {post_id} eliminado.")
        else:
            print("Post no encontrado.")
    
    def mostrar_feed(self, num_posts=10):
        feed = sorted(self.posts, key=lambda p: p.fecha_creacion, reverse=True)[:num_posts]
        for post in feed:
            print(post.mostrar())
    
    def mostrar_feed_seguidos(self, num_posts=10):
        feed = []
        for seguido in self.seguidos:
            feed.extend(seguido.posts)
        feed = sorted(feed, key=lambda p: p.fecha_creacion, reverse=True)[:num_posts]
        for post in feed:
            print(post.mostrar())
    

class Post:
    def __init__(self, usuario, texto):
        self.id = str(uuid.uuid4())
        self.usuario = usuario
        self.texto = texto
        self.fecha_creacion = datetime.now()
        self.likes = set()
    
    def dar_like(self, usuario):
        if usuario != self.usuario:
            self.likes.add(usuario)
            print(f"Like dado por {usuario.nombre}.")
        else:
            print("No puedes dar like a tu propio post.")
    
    def quitar_like(self, usuario):
        if usuario in self.likes:
            self.likes.remove(usuario)
            print(f"Like quitado por {usuario.nombre}.")
        else:
            print(f"{usuario.nombre} no había dado like a este post.")
    
    def mostrar(self):
        return f"Post ID: {self.id}\nUsuario: {self.usuario.nombre} | Texto: {self.texto}\nFecha: {self.fecha_creacion}\nLikes: {len(self.likes)}"


# Interacción con el sistema
if __name__ == "__main__":
    # Crear usuarios
    usuario1 = Usuario("Alice")
    usuario2 = Usuario("Bob")
    
    # Crear posts
    usuario1.crear_post("¡Este es mi primer post!")
    usuario2.crear_post("¡Este es el post de Bob!")
    
    # Seguir usuarios
    usuario1.seguir(usuario2)
    
    # Dar like a un post
    post_bob = usuario2.posts[0]
    usuario1.dar_like(post_bob)
    
    # Mostrar feeds
    print("\nFeed de Alice (mis posts):")
    usuario1.mostrar_feed()
    
    print("\nFeed de Alice (posts de los que sigo):")
    usuario1.mostrar_feed_seguidos()
    
    # Eliminar post
    usuario1.eliminar_post(post_bob.id)
    
    # Mostrar feed después de eliminar
    print("\nFeed de Alice (posts de los que sigo) después de eliminar:")
    usuario1.mostrar_feed_seguidos()
