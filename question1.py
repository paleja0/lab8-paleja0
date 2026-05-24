"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md

import sys

def main():
    try:
        # Se verifica que existan los argumentos necesarios (el nombre del script cuenta como el primero)
        if len(sys.argv) < 3:
            raise ValueError("Missing arguments")
        
        # Intentar convertir los argumentos a flotante y entero
        total_load = float(sys.argv[1])
        num_supports = int(sys.argv[2])
        
        # Validar división por cero antes de operar
        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
            return

        # Calcular y mostrar el resultado con 2 decimales
        load_per_support = total_load / num_supports
        print(f"Load per support point: {load_per_support:.2f} N")

    except ValueError:
        # Captura si no son números o si faltan argumentos
        print("Error: Invalid input! Enter numeric values only.")

if __name__ == "__main__":
    main()
