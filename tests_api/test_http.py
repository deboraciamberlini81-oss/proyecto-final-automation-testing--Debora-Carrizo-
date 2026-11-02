
from utils.http import get, post, put, patch, delete


def test_get_posts():
    """Verifica la consulta de publicaciones."""
    respuesta = get("posts")

    assert respuesta.status_code == 200

    publicaciones = respuesta.json()

    assert len(publicaciones) == 100
    assert publicaciones[0]["id"] == 1


def test_post_crear_publicacion():
    """Verifica la creación de una publicación."""
    datos = {
        "title": "Prueba QA",
        "body": "Publicacion creada desde Pytest",
        "userId": 1
    }

    respuesta = post("posts", datos)

    assert respuesta.status_code == 201

    resultado = respuesta.json()

    assert resultado["title"] == datos["title"]
    assert resultado["body"] == datos["body"]
    assert resultado["userId"] == datos["userId"]
    assert "id" in resultado


def test_put_actualizar_publicacion():
    """Verifica la actualización completa de una publicación."""
    datos = {
        "id": 1,
        "title": "Titulo actualizado QA",
        "body": "Contenido actualizado",
        "userId": 1
    }

    respuesta = put("posts/1", datos)

    assert respuesta.status_code == 200

    resultado = respuesta.json()

    assert resultado["title"] == datos["title"]
    assert resultado["body"] == datos["body"]
    assert resultado["userId"] == datos["userId"]


def test_patch_modificar_publicacion():
    """Verifica la modificación parcial de una publicación."""
    datos = {
        "title": "Titulo modificado con PATCH"
    }

    respuesta = patch("posts/1", datos)

    assert respuesta.status_code == 200

    resultado = respuesta.json()

    assert resultado["title"] == datos["title"]
    assert resultado["id"] == 1
    assert "body" in resultado


def test_delete_eliminar_publicacion():
    """Verifica la eliminación de una publicación."""
    respuesta = delete("posts/1")

    assert respuesta.status_code == 200
    assert respuesta.json() == {}
