from automatizador_lotes_funciones import obtener_datos_usuario, obtener_posts_usuario, guardar_reporte, guardar_reporte_general, cantidad_usuarios, buscar_usuario_ciudad

lista_general = []
# Bucle principal de automatización por lotes
cantidad = cantidad_usuarios()
for id_usuario in range(1, cantidad + 1):
    usuario, status_code = obtener_datos_usuario(id_usuario)
    
    if usuario is not None:
        # Obtenemos los posts del usuario actual
        posts = obtener_posts_usuario(id_usuario)
        
        print(f"Procesando usuario: {usuario['name']} (Ciudad: {usuario['address']['city']})")

        # Estructuración limpia del reporte incluyendo los posts
        reporte_final = {
            "nombre": usuario['name'],
            "email": usuario['email'],
            "ciudad": usuario['address']['city'],
            "cantidad_posts": len(posts)
        }

        lista_general.append(reporte_final)
        # Persistencia utilizando la capa de servicios
        guardar_reporte(id_usuario, reporte_final)
        print(f"-> Reporte del usuario {id_usuario} guardado con éxito con {len(posts)} posts.\n")
        
    else:
        print(f"-> Error: El servidor respondió con código {status_code}. No se pudo procesar el usuario {id_usuario}.\n")


if len(lista_general)> 0:
    guardar_reporte_general(lista_general)
    print("La lista general de usuarios se ha guardado con exito")

ciudad_a_buscar = input("Ingresa el nombre de una ciudad para buscar usuarios (ej. Gwenborough): ")
buscar_usuario_ciudad(ciudad_a_buscar)