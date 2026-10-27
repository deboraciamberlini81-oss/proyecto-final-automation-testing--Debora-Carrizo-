
import time

import pytest
import requests
from faker import Faker

fake = Faker()
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.e2e
def test_ciclo_vida_post():
    inicio = time.perf_counter()

    # 1. POST: crear un post con datos aleatorios
    payload = {
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": 1,
    }

    respuesta_post = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=3,
    )

    assert respuesta_post.status_code == 201
    post_creado = respuesta_post.json()

    # Validar esquema, tipos e ID
    assert isinstance(post_creado, dict)
    assert {"id", "title", "body", "userId"}.issubset(
        post_creado.keys()
    )
    assert isinstance(post_creado["id"], int)
    assert isinstance(post_creado["title"], str)
    assert isinstance(post_creado["body"], str)

    post_id = post_creado["id"]
    assert post_id > 0

    # 2. PATCH: actualizar el título
    nuevo_titulo = "Título actualizado por QA"

    respuesta_patch = requests.patch(
        f"{BASE_URL}/posts/{post_id}",
        json={"title": nuevo_titulo},
        timeout=3,
    )

    assert respuesta_patch.status_code == 200
    post_actualizado = respuesta_patch.json()
    
    

    assert isinstance(post_actualizado, dict)
    assert post_actualizado["title"] == nuevo_titulo
    assert isinstance(post_actualizado["title"], str)

    # 3. DELETE: eliminar el post
    respuesta_delete = requests.delete(
        f"{BASE_URL}/posts/{post_id}",
        timeout=3,
    )

    assert respuesta_delete.status_code == 200

    # 4. Validar tiempo total del flujo
    tiempo_total = time.perf_counter() - inicio

    print(f"ID del post: {post_id}")
    print(f"Título actualizado: {nuevo_titulo}")
    print(f"Tiempo total: {tiempo_total:.3f} segundos")

    assert tiempo_total < 3, (
        f"El flujo tardó {tiempo_total:.3f} segundos; "
        "el máximo permitido es 3 segundos"
    )
