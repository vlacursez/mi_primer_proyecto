def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo 'n' de forma iterativa.
    
    El factorial de n (n!) es el producto de todos los enteros positivos menores o 
    iguales a n (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120).

    Args:
        n (int): El número del cual se calculará el factorial.

    Returns:
        int: El valor del factorial de 'n'.
    """
    if n < 0:
        # El factorial no está definido para números negativos
        raise ValueError("El factorial solo está definido para números enteros no negativos.")
    
    if n == 0 or n == 1:
        return 1
    
    # Cálculo iterativo
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
        
    return resultado

def main():
    """Función principal para solicitar la entrada del usuario y mostrar el resultado."""
    try:
        # Pide al usuario el número
        n = int(input("Ingresa el número para calcular su factorial (e.g., 5): "))
        
        # Calcula y muestra el factorial
        resultado = calcular_factorial(n)
        print(f"\n✅ El factorial de {n} es: {resultado}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")

# Ejecución principal
if __name__ == "__main__":
    main()