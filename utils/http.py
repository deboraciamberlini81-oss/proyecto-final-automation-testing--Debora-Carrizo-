
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15


def get(endpoint, params=None):
    """Realiza una consulta GET."""
    return requests.get(
        f"{BASE_URL}/{endpoint.lstrip('/')}",
        params=params,
        timeout=TIMEOUT,
    )


def post(endpoint, payload):
    """Crea un recurso mediante POST."""
    return requests.post(
        f"{BASE_URL}/{endpoint.lstrip('/')}",
        json=payload,
        timeout=TIMEOUT,
    )


def put(endpoint, payload):
    """Reemplaza un recurso mediante PUT."""
    return requests.put(
        f"{BASE_URL}/{endpoint.lstrip('/')}",
        json=payload,
        timeout=TIMEOUT,
    )


def patch(endpoint, payload):
    """Actualiza parcialmente un recurso."""
    return requests.patch(
        f"{BASE_URL}/{endpoint.lstrip('/')}",
        json=payload,
        timeout=TIMEOUT,
    )


def delete(endpoint):
    """Elimina un recurso mediante DELETE."""
    return requests.delete(
        f"{BASE_URL}/{endpoint.lstrip('/')}",
        timeout=TIMEOUT,
    )
