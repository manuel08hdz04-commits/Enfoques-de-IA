#¿Qué es un Algoritmo Genético?
# Los Algoritmos Genéticos son métodos de optimización inspirados en la teoría de la evolución de 
# Darwin. A diferencia de otros algoritmos que mueven un solo "explorador" por el mapa, estos 
# trabajan con una población completa de soluciones simultáneamente.

#Cómo funciona:
# Fitness (Aptitud): Es una función que mide qué tan "buena" es una solución. En nuestro caso, 
# entre más cerca esté de la meta (menor heurística), mayor es su aptitud.
# Selección: Los individuos más aptos tienen más probabilidades de sobrevivir y reproducirse.
# Elitismo: Técnica donde los mejores individuos de una generación pasan intactos a la siguiente 
# para asegurar que no se pierda el progreso.
# Mutación/Crossover: En este código simplificado, la "descendencia" es un salto hacia un nodo 
# vecino, simulando una pequeña mutación en el ADN de la solución.

import random

# Mapa de rutas de mutación genética
linajes_microbios = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Tabla de Aptitud (Distancia al ADN perfecto 'F')
# Usamos valores negativos porque buscamos maximizar la cercanía
radar_aptitud = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

CATALOGO_COMPLETO = list(linajes_microbios.keys())

def evaluar_supervivencia(especie):
    """Calcula el Fitness: entre menos distancia a 'F', mejor."""
    return -radar_aptitud[especie]

def elegir_progenitor(cultivo):
    """Selecciona un espécimen al azar del cultivo actual."""
    return random.choice(cultivo)

def mutar_especimen(progenitor):
    """Genera un descendiente basado en las conexiones genéticas."""
    mutaciones_posibles = linajes_microbios[progenitor]
    
    if mutaciones_posibles:
        # El hijo muta a un estado vecino
        return random.choice(mutaciones_posibles)
    else:
        # Salto genético aleatorio si llega a un callejón sin salida
        return random.choice(CATALOGO_COMPLETO)

def simulacion_evolutiva():
    """
    Ejecuta el ciclo de vida de una población de microbios buscando el ADN 'F'.
    """
    # Población inicial (Nivel de complejidad bajo)
    cultivo = ['A', 'B', 'C']
    num_generaciones = 5

    print("--- Iniciando Ciclo Evolutivo de Laboratorio ---")

    for ciclo in range(num_generaciones):
        # Clasificamos por aptitud (de mayor a menor)
        cultivo = sorted(cultivo, key=evaluar_supervivencia, reverse=True)
        print(f"Generación {ciclo} (Líder: {cultivo[0]}): {cultivo}")

        # Aplicamos ELITISMO: El 66% de los mejores sobrevive sin cambios
        proxima_generacion = cultivo[:2] 

        # REPRODUCCIÓN: Completamos el cultivo con nuevos descendientes
        while len(proxima_generacion) < len(cultivo):
            ancestro = elegir_progenitor(cultivo)
            descendiente = mutar_especimen(ancestro)
            proxima_generacion.append(descendiente)

        cultivo = proxima_generacion

    # Resultado final de la evolución
    especimen_dominante = max(cultivo, key=evaluar_supervivencia)
    print(f"\nResultado final de la evolución: {especimen_dominante}")
    if especimen_dominante == 'F':
        print("¡ÉXITO! Se ha alcanzado el estado de ADN perfecto.")

# --- INICIO DEL EXPERIMENTO ---
simulacion_evolutiva()