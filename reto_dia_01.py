while True:
    nombre = input("Cual es tu nombre?: ")
    try:

        if nombre == "":
            print("El nombre no puede estar vacío. Intenta de nuevo.\n")
            continue    
        break
    except ValueError:
        print(f"{nombre} no es un nombre válido. Debes ingresar un valor de texto (ej: Juan).\n")

while True:
    horno_temperatura = input("Cual es la temperatura del horno?")
    try:
        temperatura = float(horno_temperatura)
        if temperatura < 0 or temperatura > 400:
            print("La temperatura debe estar entre 0 y 400 grados. Intenta de nuevo.\n")
            continue
        break
    except ValueError:
        print(f"{horno_temperatura} no es un número válido. Debes ingresar un valor numérico (ej: 180).\n")

if temperatura < 150:
    estado = "Precalentamiento / Frío"
elif temperatura <= 260:
    estado = "Temperatura Óptima de Operación"
else:
    estado = "¡ALERTA: Sobrecalentamiento peligroso!"

   # 5. Salida formateada con 2 decimales (.2f)
print("\n" + "=" * 40)  
print(f"Operador:              {nombre}")
print(f"Temperatura del horno: {temperatura:.1f} grados") 
print(f"Estado del equipo:     {estado}")  
print("\n" + "=" * 40)  

    