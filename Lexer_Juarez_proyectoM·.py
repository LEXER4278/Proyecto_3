#Alumno: Lexer Iván Juárez Vargas el 28/11/2024
#Recreacion de una maquina de galton donde se soltaran 3,000 canicas con 12 niveles de obstaculos y mostrando el resultado 
import random
import matplotlib.pyplot as plt

# Función que simula el recorrido de una canica y la eleccion aleatoria de izquieda (-1) o derecha (1)
def simular_canica(nivel_obstaculos):
    posicion = 0
    for _ in range(nivel_obstaculos):
        posicion += random.choice([-1, 1])
    return posicion

# Función que simula la máquina de Galton con varias canicas
def simular_maquina_de_galton(cantidad_canicas, nivel_obstaculos):
    resultados = [0] * (2 * nivel_obstaculos + 1) 
    for _ in range(cantidad_canicas):
        resultado_canica = simular_canica(nivel_obstaculos)
        resultados[resultado_canica + nivel_obstaculos] += 1 
    return resultados


#Función para graficar con matplotlin
def graficar_histograma(resultados,nivel_obstaculos):
    contenedores = list(range(-nivel_obstaculos,nivel_obstaculos + 1))
    plt.bar(contenedores,resultados,color ="red", edgecolor = "black")
    plt.title("Maquina de galton")
    plt.xlabel("Contenedor")
    plt.ylabel("Número de canicas")
    plt.show()



# Parámetros de la simulación 
cantidad_canicas = 3000
nivel_obstaculos = 12

# Ejecutar la simulación
resultados = simular_maquina_de_galton(cantidad_canicas, nivel_obstaculos)

# Graficar los resultados con matplotlib
graficar_histograma(resultados, nivel_obstaculos)
