#Alumno: Lexer Iván Juárez Vargas el 28/11/2024
#Recreacion de una maquina de galton donde se soltaran 3,000 canicas con 12 niveles de obstaculos y mostrando el resultado 
import random

# Función que simula el recorrido de una canica
def simular_canica(nivel_obstaculos):
    posicion = 0
    for _ in range(nivel_obstaculos):
        posicion += random.choice([-1, 1])
    return posicion

# Función que simula la máquina de Galton con varias canicas
def simular_maquina_de_galton(cantidad_canicas, nivel_obstaculos):
    resultados = [0] * (2 * nivel_obstaculos + 1)  # Ajustar la longitud de la lista
    for _ in range(cantidad_canicas):
        resultado_canica = simular_canica(nivel_obstaculos)
        resultados[resultado_canica + nivel_obstaculos] += 1  # Ajustar índice para valores negativos
    return resultados

# Función para mostrar un histograma de texto
def imprimir_histograma(resultados, nivel_obstaculos):
    contenedores = list(range(-nivel_obstaculos, nivel_obstaculos + 1))
    max_altura = max(resultados)
    print("\nHistograma de la Máquina de Galton")
    print("Contenedor | Número de Canicas | Histograma")
    print("-" * 40)
    for contenedor, canicas in zip(contenedores, resultados):
        barras = '*' * (canicas * 40 // max_altura)  # Escalar barras para caber en la pantalla
        print(f"{contenedor:^10} | {canicas:^17} | {barras}")

# Parámetros de la simulación
cantidad_canicas = 10000
nivel_obstaculos = 12

# Ejecutar la simulación
resultados = simular_maquina_de_galton(cantidad_canicas, nivel_obstaculos)

# Mostrar el histograma
imprimir_histograma(resultados, nivel_obstaculos)
