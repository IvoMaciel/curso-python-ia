# 04_funciones.py - Funciones y código modular

# 1. Definimos una función reutilizable para pedir números con validación
def pedir_numero(mensaje, minimo, maximo):
    """Pide un número al usuario y no avanza hasta que esté dentro del rango."""
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor < minimo or valor > maximo:
                print(f"Error: El valor debe estar entre {minimo} y {maximo}.\n")
                continue
            return valor  # 'return' entrega el número y termina la función
        except ValueError:
            print(f"Error: '{entrada}' no es un número válido.\n")


# 2. Definimos una función para realizar cálculos
def calcular_promedio(n1, n2, n3):
    """Calcula y devuelve el promedio de tres números."""
    return (n1 + n2 + n3) / 3


# --- PROGRAMA PRINCIPAL ---
print("=== SISTEMA DE CALIFICACIONES (MODULAR) ===")

nombre = input("Nombre del estudiante: ")

# ¡Mira qué limpio queda pedir 3 notas usando la misma función una y otra vez!
nota1 = pedir_numero("Ingresa la Nota 1 (0 a 20): ", 0, 20)
nota2 = pedir_numero("Ingresa la Nota 2 (0 a 20): ", 0, 20)
nota3 = pedir_numero("Ingresa la Nota 3 (0 a 20): ", 0, 20)

promedio = calcular_promedio(nota1, nota2, nota3)

print("\n" + "=" * 35)
print(f"Estudiante: {nombre}")
print(f"Promedio final: {promedio:.2f}")

if promedio >= 10:
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")
print("=" * 35)