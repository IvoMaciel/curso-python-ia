# 03_calculadora.py - División de cuenta con control de errores

print("--- CALCULADORA DE CUENTAS COMPARTIDAS ---")

# 1. Validar el total de la cuenta (acepta decimales con float)
while True:
    total_texto = input("Total de la cuenta en $, ")
    try:
        total = float(total_texto)
        if total <= 0:
            print("El total debe ser mayor que cero. Intenta de nuevo.\n")
            continue
        break
    except ValueError:
        print(f"{total_texto} no es un número válido. Debes ingresar un valor numérico (ej: 100.50).\n")

       # 2. Validar porcentaje de propina
while True:
    propina_texto = input("Porcentaje de propina deseado (ej: 10, 15, 20): ")
    try:
        propina = float(propina_texto)
        if propina < 0:
            print("El porcentaje de propina no puede ser negativo. Intenta de nuevo.\n")
            continue
        break
    except ValueError:
        print(f"{propina_texto} no es un número válido. Debes ingresar un valor numérico (ej: 15).\n")  


        # 3. Validar cantidad de personas (debe ser entero y mayor a 0)
while True:
    personas_texto = input("Cantidad de personas para dividir la cuenta: ")
    try:
        personas = int(personas_texto)
        if personas <= 0:
            print("La cantidad de personas debe ser mayor que cero. Intenta de nuevo.\n")
            continue
        break
    except ValueError:
        print(f"{personas_texto} no es un número válido. Debes ingresar un valor entero (ej: 3).\n")

        # 4. Cálculos matemáticos
monto_propina = total * (propina / 100)
total_final = total + monto_propina
pago_por_persona = total_final / personas

        # 5. Salida formateada con 2 decimales (.2f)
print("\n" + "=" * 40)
print(f"Subtotal:           ${total:.2f}")
print(f"Propina ({propina:.0f}%):       ${monto_propina:.2f}")
print(f"Total a pagar:      ${total_final:.2f}")
print(f"Cada persona paga:  ${pago_por_persona:.2f}")
print("=" * 40)



    