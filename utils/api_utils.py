import os
import requests
API_KEY = os.getenv("REQRES_API_KEY")

HEADERS = {
    "x-api-key": API_KEY
} if API_KEY else {}


BASE_URL = "https://reqres.in/api"


def obtener_usuarios(page=1):
    """Obtiene una página de usuarios desde la API."""
    return requests.get(
        f"{BASE_URL}/users",
        params={"page": page},
        headers=HEADERS,
        timeout=15,
    )


def iniciar_sesion(email, password=None):
    """Envía las credenciales a la API de login."""
    payload = {"email": email}

    if password:
        payload["password"] = password

    return requests.post(
        f"{BASE_URL}/login",
        json=payload,
        headers=HEADERS,
        timeout=15,
    )
def crear_usuario(payload):
    """Crea un usuario nuevo en la API."""
    return requests.post(
        f"{BASE_URL}/users",
        json=payload,
        headers=HEADERS,
        timeout=15,
    )