import requests
import json
import os
from dotenv import load_dotenv
from automatizador_lotes_funciones import obtener_datos_usuario, obtener_posts_usuario, guardar_reporte

# Revisa si existe una carpeta llamada reportes. Si no existe, créala automáticamente". Esto se hace con una sola línea de código estandarizada:
# Carga las variables de entorno definidas en el archivo .env oculto
load_dotenv()
api_key = os.getenv("API_BASE_URL")

for id_usuario in range(1, 6):
    usuario, status_code = obtener_datos_usuario(api_key, id_usuario)
    if usuario is not None:
        usuario_post = obtener_posts_usuario(id_usuario, api_key)
        print(f"El nombre del usuario es {usuario['name']} y vive en la ciudad {usuario['address']['city']} en la calle {usuario['address']['street']}")
        print(f"Numero de publicaciones del usuario {len(usuario_post)}")

        nombre = usuario['name']
        ciudad = usuario['address']['city']
        calle = usuario['address']['street']
        cantidad_post = len(usuario_post)
    
    # Crea un diccionario estructurado limpio con la información procesada
        reporte_final = {"nombre": nombre, "ciudad": ciudad, "calle": calle, "cantidad": cantidad_post}
        print(reporte_final)

    # 6. Persistencia local: Guarda el diccionario en un archivo JSON dinámico en el disco duro
        guardar_reporte(id_usuario, reporte_final)
    else: 
    # Control de errores si el ID ingresado no existe en el servidor (ej. código 404)
        print(f"Error: El servidor respondió con código {status_code}. El usuario no existe.")
        continue

