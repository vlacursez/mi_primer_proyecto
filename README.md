# calculadora.py
# Script básico para operaciones matemáticas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

# Bloque de ejecución con indentación correcta
if operacion == '+':
    print("Resultado:", numero_1 + numero_2)
elif operacion == '-':
    print("Resultado:", numero_1 - numero_2)
elif operacion == '*':
    print("Resultado:", numero_1 * numero_2)
elif operacion == '/':
    # Se corrige la referencia a la variable (numero_2 en lugar de b)
    if numero_2 != 0:
        print("Resultado:", numero_1 / numero_2)
    else:
        print("Error: no se puede dividir por cero.") # Manejo de división por cero
else:
    print("Operación no válida.")# mi_primer_proyecto
