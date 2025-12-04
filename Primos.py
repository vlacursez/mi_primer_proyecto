def es_primo(n):
    """
    Verifica si un número entero positivo es primo.

    Un número primo es un número natural mayor que 1 que tiene solo 
    dos divisores positivos distintos: él mismo y 1.

    Args:
        n (int): El número a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    # 1. Los números menores o iguales a 1 no son primos.
    if n <= 1:
        return False
        
    # 2. El 2 es el único número par primo.
    if n == 2:
        return True
        
    # 3. Si es par (y mayor que 2), no es primo.
    if n % 2 == 0:
        return False

    # 4. Comprobación de divisibilidad hasta la raíz cuadrada de n.
    # No necesitamos verificar divisores más allá de la raíz cuadrada de n.
    # Usamos n ** 0.5 para calcular la raíz cuadrada.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False  # Se encontró un divisor, no es primo
        # Solo necesitamos verificar números impares
        i += 2 
        
    return True # No se encontraron divisores, es primo

def main():
    """Función principal para solicitar la entrada del usuario y mostrar el resultado."""
    try:
        # Pide al usuario el número
        entrada = input("Ingresa un número entero para verificar si es primo: ")
        n = int(entrada)
        
        # Evalúa el número
        if es_primo(n):
            print(f"\n✅ El número {n} ES un número primo.")
        else:
            print(f"\n❌ El número {n} NO es un número primo.")
            
    except ValueError:
        print("\n❌ Entrada no válida. Por favor, ingresa un número entero.")

# Ejecución principal
if __name__ == "__main__":
    main()