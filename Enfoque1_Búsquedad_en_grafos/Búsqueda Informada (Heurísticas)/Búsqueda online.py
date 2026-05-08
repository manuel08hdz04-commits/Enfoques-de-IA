#¿Qué es la Búsqueda Online?
#A diferencia de los algoritmos "Offline" (como A* o BFS), donde el agente planea toda la ruta antes 
# de dar el primer paso, en la Búsqueda Online el agente explora y aprende del entorno mientras se 
# mueve.

#Cómo funciona:
# Conocimiento Local: El agente solo conoce los nodos vecinos del lugar donde está parado actualmente.
# Toma de Decisiones Inmediata: En cada paso, el agente evalúa sus opciones inmediatas y elige la que 
# parece mejor (generalmente usando una heurística), sin saber qué hay más allá.
# Interactividad: Es el modelo ideal para robots en entornos dinámicos o videojuegos donde el mapa 
# se revela conforme el personaje camina (la famosa "Niebla de Guerra").

# Mapa de pasillos (Solo revelado al estar físicamente en el nodo)
laberinto_desconocido = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Sensor de proximidad (Heurística): Señal captada desde la posición actual
sensor_señal = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# --- SISTEMA DE TELEMETRÍA ---
def registrar_pasos_explorador(bitacora, sistema):
    """Muestra la ruta exacta que el explorador fue descubriendo."""
    print(f"[{sistema}] Trazado de ruta en vivo:")
    for i, punto in enumerate(bitacora):
        print(f"Movimiento {i}: Sector {punto}")

# --- BÚSQUEDA ONLINE ---
def protocolo_exploracion_online(punto_partida, punto_meta):
    """
    El agente toma decisiones paso a paso sin conocer el grafo completo.
    """
    ubicacion_actual = punto_partida
    bitacora_vuelo = [ubicacion_actual]

    print(f"--- Iniciando Búsqueda Online desde '{punto_partida}' ---")

    # El agente sigue moviéndose mientras no alcance la meta
    while ubicacion_actual != punto_meta:
        # El agente 'mira' a su alrededor (solo ve vecinos directos)
        opciones_adyacentes = laberinto_desconocido[ubicacion_actual]
        
        if not opciones_adyacentes:
            print("¡ERROR! El explorador ha entrado en un callejón sin salida.")
            break

        # Toma la decisión basada en la mejor lectura de sensor inmediata
        # El agente es 'miope': no sabe si después de C hay una pared, pero C brilla más.
        siguiente_paso = min(opciones_adyacentes, key=lambda x: sensor_señal[x])
        
        ubicacion_actual = siguiente_paso
        bitacora_vuelo.append(ubicacion_actual)

    registrar_pasos_explorador(bitacora_vuelo, "Exploración Online")
    
    if ubicacion_actual == punto_meta:
        print(f"Confirmación: Objetivo '{punto_meta}' alcanzado con éxito.")

# --- INICIO DE LA MISIÓN ---
protocolo_exploracion_online('A', 'F')