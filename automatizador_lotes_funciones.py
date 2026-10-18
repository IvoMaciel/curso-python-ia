import requests
import os
import json

def obtener_datos_usuario(api_key, id_usuario):
    try:
        # Intentamos hacer la petición a la red
        respuesta = requests.get(f"{api_key}/users/{id_usuario}", timeout=5)
        if respuesta.status_code == 200:
            return respuesta.json(), respuesta.status_code
        else:
            return None, respuesta.status_code
    except requests.exceptions.RequestException as error:
        # Si la red falla por completo, capturamos el error sin que el script se rompa
        print(f"[ERROR DE RED] No se pudo conectar al servidor: {error}")
        return None, 500


def obtener_posts_usuario(id_usuario, api_base):
    respuesta_post = requests.get(f"{api_base}/posts?userId={id_usuario}")
    if respuesta_post.status_code == 200:
        return respuesta_post.json()
    else:
        # Corregido: Agregamos el return para que devuelva la lista vacía
        return []

def guardar_reporte(id_usuario, datos_reporte):
    os.makedirs("reportes", exist_ok=True)
    with open(f"reportes/reporte_usuario_{id_usuario}.json", "w", encoding="utf8") as archivo:
        json.dump(datos_reporte, archivo, indent=4, ensure_ascii=False)