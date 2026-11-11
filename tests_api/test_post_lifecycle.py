import time

import pytest
import requests
from faker import Faker

fake = Faker()
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.e2e
def test_ciclo_vida_post():
    # Preparar datos de prueba
    payload = {
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": 1,
    }

    # 1. POST: crear una publicación
    inicio = time.perf_counter()

    respuesta_post = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=3,
    )

    assert respuesta_post.status_code == 201
    post_creado = respuesta_post.json()

    # Validar estructura y datos
    assert isinstance(post_creado, dict)
    assert {"id", "title", "body", "userId"}.issubset(
        post_creado.keys()
    )
    assert isinstance(post_creado["id"], int)
    assert post_creado["id"] > 0
    assert post_creado["title"] == payload["title"]
    assert post_creado["body"] == payload["body"]
    assert post_creado["userId"] == payload["userId"]

    post_id = post_creado["id"]

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

    # 3. DELETE: eliminar la publicación
    respuesta_delete = requests.delete(
        f"{BASE_URL}/posts/{post_id}",
        timeout=3,
    )

    assert respuesta_delete.status_code == 200

    # 4. Registrar el tiempo total del ciclo
    tiempo_total = time.perf_counter() - inicio

    print(f"ID de la publicación: {post_id}")
    print(f"Título actualizado: {nuevo_titulo}")
    print(f"Tiempo total del ciclo: {tiempo_total:.3f} segundos")
