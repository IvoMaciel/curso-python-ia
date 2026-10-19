import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

def obtener_datos_usuario(id_usuario):
    """Consulta la API para obtener los datos de un usuario de forma segura."""
    try:
        url = f"{API_BASE_URL}/users/{id_usuario}"
        respuesta = requests.get(url, timeout=5)
        
        if respuesta.status_code == 200:
            return respuesta.json(), respuesta.status_code
        else:
            return None, respuesta.status_code
            
    except requests.exceptions.RequestException as error:
        print(f"[ERROR DE RED] No se pudo conectar al servidor para el usuario {id_usuario}: {error}")
        return None, 500

def obtener_posts_usuario(id_usuario):
    """Consulta las publicaciones asociadas a un usuario específico."""
    try:
        url = f"{API_BASE_URL}/posts?userId={id_usuario}"
        respuesta = requests.get(url, timeout=5)
        
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return []
            
    except requests.exceptions.RequestException as error:
        print(f"[ERROR DE RED] Falló la conexión al obtener posts: {error}")
        return []

def guardar_reporte(id_usuario, datos_reporte):
    """Crea la carpeta 'reportes' si no existe y guarda el JSON estructurado."""
    os.makedirs("reportes", exist_ok=True)
    ruta_archivo = f"reportes/reporte_usuario_{id_usuario}.json"
    
    with open(ruta_archivo, "w", encoding="utf8") as archivo:
        json.dump(datos_reporte, archivo, indent=4, ensure_ascii=False)

def guardar_reporte_general(lista_general):
    os.makedirs("reportes", exist_ok=True)
    ruta_archivo = f"reportes/reporte_general.json"

    with open(ruta_archivo, "w", encoding="utf8") as archivo:
            json.dump(lista_general, archivo, indent=4, ensure_ascii=False)


def cantidad_usuarios():
    while True:
        try:
            cantidad_usuarios= int(input("Cuantos usuarios deseas procesar?: "))
            if cantidad_usuarios > 0:
                return cantidad_usuarios
            else:
                print("La cantidad de usuarios debe ser mayor a cero (0)")
        except ValueError:
            print(f"Error: {cantidad_usuarios} no es un numero valido")


def buscar_usuario_ciudad(ciudad):
    ruta_archivo = f"reportes/reporte_general.json"
    try:
        with open(ruta_archivo, "r", encoding="utf8") as archivo:
            usuario = json.load(archivo)
    except (json.JSONDecodeError, OSError, FileNotFoundError):
        print("No se pudieron leer los datos.")
        return []
    
    encontrado = False
    for lugar in usuario:
        if ciudad.strip().lower() == lugar['ciudad'].strip().lower():
            print(f"Usuario: {lugar['nombre']} Email: {lugar['email']} Ciudad: {lugar['ciudad']} Cantidad Posts: {lugar['cantidad_posts']}")
            encontrado = True
            
    if not encontrado:
        print(f"No se encontraron usuarios en la ciudad: {ciudad}")
            

    
