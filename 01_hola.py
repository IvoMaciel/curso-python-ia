nombre = input("Por favor, introduce tu nombre: ")
edad_texto = input("Introduce tu edad: ")

try:
    # Intentamos la conversión matemática
    edad = int(edad_texto)

    # Validamos que no metan números negativos o irreales
    if edad < 0 or edad > 120:
        print(f"Error: {edad} no parece una edad válida.")
    else:
        if edad >= 18:
            estado = "mayor de edad"
        else:
            estado = "menor de edad"
        
        print(f"\n¡Hola, {nombre}! Tienes {edad} años y eres {estado}.")
        print("¡El script se ejecutó sin fallos!")

        # Este bloque solo se activa si el usuario escribió letras en vez de números
except ValueError:
    print(f"\nError: '{edad_texto}' no es un número válido. Debes ingresar digitos ejemplo(55)")
