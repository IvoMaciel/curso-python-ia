def pedir_numero(mensaje, minimo, maximo):
    """Función defensiva para pedir números en un rango."""
    while True:
        entrada = input(mensaje)
        try:
            valor= float(entrada)
            if valor < minimo or valor > maximo:
                print(f"Ingrese un numero valido entre {minimo} y {maximo}")
                continue
            return valor
        except ValueError:
            print(f"Error: '{entrada}' no es un número válido.\n")

inventario = []

numero_productos = int(pedir_numero("¿Cuántos productos ingresarás al inventario? (1 a 10): ", 1, 10))

for i in range(1,numero_productos+1):
    while True:
        nombre = input(f"Ingresa el nombre del producto #{i}: ").strip()
        if nombre == "":
            print("Error: El nombre del producto no puede estar vacío. Intenta de nuevo.\n")
            continue  # Volvemos al inicio del bucle para pedir el nombre nuevamente
        break
   
    precio = pedir_numero(f"Ingresa el precio del producto #{i} (001 a 10000): ", 0.01, 10000)
    cantidad = pedir_numero(f"Ingresa la cantidad del producto #{i} (1 a 1000): ", 1, 1000)

    # Guardamos cada producto como un diccionario

    producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
    "subtotal": precio * cantidad
}
   # 
    inventario.append(producto)

# --- REPORTE GENERAL ---
print("\n" + "=" * 55)
print("REPORTE GENERAL DEL INVENTARIO")
print("=" * 55)

valor_total_almacen = 0.0

for producto in inventario:
    print("\n" + "=" * 45)
    print("FICHA DEL PRODUCTO (DICCIONARIO EN MEMORIA):")
    print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']} | Subtotal: {producto['subtotal']:.2f}")
    valor_total_almacen += producto["subtotal"]

print("-" * 55)
print(f"VALOR TOTAL EN MERCANCÍA: ${valor_total_almacen:.2f}")
print("=" * 55)   
    
      





