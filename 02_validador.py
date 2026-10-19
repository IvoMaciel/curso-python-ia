# 02_validador.py - Bucle de validación interactiva

nombre = input("Por favor, introduce tu nombre: ")

# Bucle infinito: no dejará avanzar hasta recibir un número correcto
while True:
    edad_texto = input("Introduce tu edad en números: ")
    
    try:
        edad = int(edad_texto)
        
        # Validamos un rango razonable
        if edad < 0 or edad > 120:
            print("Error: Ingresa una edad lógica entre 0 y 120 años.\n")
            continue  # Vuelve a empezar el bucle
            
        # Si todo está bien, salimos del bucle con 'break'
        break

    except ValueError:
        print(f"Error: '{edad_texto}' no es válido. Debes usar dígitos (ej: 25, 40, 55).\n")

# Una vez superado el bucle, clasificamos
if edad >= 65:
    categoria = "Adulto Mayor"
elif edad >= 18:
    categoria = "Adulto"
else:
    categoria = "Menor de edad"

print("-" * 40)
print(f"Ficha registrada: {nombre}")
print(f"Edad: {edad} años | Categoría: {categoria}")
print("-" * 40)