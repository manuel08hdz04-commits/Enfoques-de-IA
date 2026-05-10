#¿Qué es la Búsqueda de la Política?
#A diferencia de otros métodos que intentan calcular el valor exacto de cada estado (como la iteración 
# de valores), la Búsqueda de la Política trabaja directamente sobre el comportamiento.

#Imagina que tienes un manual de instrucciones. En lugar de calcular cuánto dinero ganarás en cada 
# habitación, simplemente cambias una instrucción del manual (ej. "en la cocina, en lugar de ir a la 
# sala, ve al comedor") y pruebas si el resultado final mejora. Si el cambio es positivo, lo conservas.

#Componentes clave:

#Espacio de Políticas: El conjunto de todas las combinaciones posibles de acciones en todos los estados.

#Función de Aptitud (Fitness): Un proceso que ejecuta la política y devuelve una puntuación 
# (recompensa total).

#Ascenso de Colinas (Hill Climbing): La técnica de hacer cambios aleatorios y solo aceptarlos si 
# mejoran la puntuación actual.

import random

# --- EL MAPA DE LA RED (Nodos y Latencia/Recompensa) ---
# El objetivo es maximizar la recompensa acumulada (eficiencia de red)
red_datos = {
    'Router_Inicio': {'Nodo_B': 1, 'Nodo_C': 5},
    'Nodo_B': {'Servidor_D': 2, 'Servidor_E': 4},
    'Nodo_C': {'Data_Center': 10},
    'Servidor_D': {},
    'Servidor_E': {'Data_Center': 1},
    'Data_Center': {}
}

# 1. GENERACIÓN DE POLÍTICA INICIAL (Manual Aleatorio)
# π(s) -> a
politica = {nodo: random.choice(list(red_datos[nodo].keys())) 
            for nodo in red_datos if red_datos[nodo]}

def evaluar_manual(manual_actual):
    """Simula el envío de un paquete usando el manual de rutas."""
    actual = 'Router_Inicio'
    puntos = 0
    camino = [actual]
    
    while red_datos[actual]:
        accion = manual_actual[actual]
        puntos += red_datos[actual][accion]
        actual = accion
        camino.append(actual)
        
    return puntos, camino

# --- PROCESO DE OPTIMIZACIÓN (BÚSQUEDA) ---
mejor_puntaje, _ = evaluar_manual(politica)

print(f"--- Iniciando Optimización de Política ---")
print(f"Puntaje inicial: {mejor_puntaje}")

for i in range(15):
    # Creamos una variante (mutación) del manual actual
    nueva_politica = politica.copy()
    
    # Elegimos un nodo al azar y cambiamos su dirección
    nodo_a_modificar = random.choice(list(politica.keys()))
    nueva_politica[nodo_a_modificar] = random.choice(list(red_datos[nodo_a_modificar].keys()))
    
    # Evaluamos la variante
    nuevo_puntaje, _ = evaluar_manual(nueva_politica)
    
    # Si la nueva instrucción es mejor, actualizamos el manual oficial
    if nuevo_puntaje > mejor_puntaje:
        politica = nueva_politica
        mejor_puntaje = nuevo_puntaje
        print(f"Iteración {i+1:02d}: ¡Mejora detectada! Nuevo máximo: {mejor_puntaje}")

# --- RESULTADO FINAL ---
puntos_finales, ruta_final = evaluar_manual(politica)

print("\n" + "="*50)
print(" MANUAL DE RUTAS OPTIMIZADO ")
print("="*50)
print(f"Ruta elegida: {' -> '.join(ruta_final)}")
print(f"Eficiencia total: {puntos_finales} ms/puntos")

print("\nConfiguración del Manual:")
for nodo, destino in politica.items():
    print(f" En {nodo.ljust(15)} -> Enviar a: {destino}")
    