# 05_estructuras.py - Listas, diccionarios y funciones

def pedir_numero(mensaje, minimo, maximo):
    """Función defensiva para pedir números en un rango."""
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor < minimo or valor > maximo:
                print(f"Error: Ingrese un valor entre {minimo} y {maximo}.\n")
                continue
            return valor
        except ValueError:
            print(f"Error: '{entrada}' no es un número válido.\n")


# --- PROGRAMA PRINCIPAL ---
print("=== REGISTRO DE CALIFICACIONES CON LISTAS Y DICCIONARIOS ===")

nombre = input("Nombre del estudiante: ").strip()

# Creamos una lista vacía para almacenar las calificaciones
calificaciones = []

# Usamos un bucle for para pedir exactamente 3 notas
for i in range(1, 4):
    nota = pedir_numero(f"Ingresa la nota #{i} (0 a 20): ", 0, 20)
    calificaciones.append(nota)  # .append() agrega la nota a la lista

# Calculamos el promedio usando funciones integradas de Python: sum() y len()
promedio = sum(calificaciones) / len(calificaciones)

# Guardamos toda la información consolidada en un DICCIONARIO
estudiante = {
    "nombre": nombre,
    "notas": calificaciones,
    "promedio": promedio,
    "aprobado": promedio >= 10
}

# Mostramos el reporte accediendo a las claves del diccionario
print("\n" + "=" * 45)
print("FICHA DEL ESTUDIANTE (DICCIONARIO EN MEMORIA):")
print(f"Nombre:   {estudiante['nombre']}")
print(f"Notas:    {estudiante['notas']}")
print(f"Promedio: {estudiante['promedio']:.2f}")

if estudiante["aprobado"]:
    print("Estado:   APROBADO")
else:
    print("Estado:   REPROBADO")
print("=" * 45)