#¿Qué son las Heurísticas y cómo funciona la Búsqueda Voraz?
# Una Heurística es un "atajo" mental o una regla práctica que ayuda a resolver un problema más rápido. 
# En algoritmos de búsqueda, es una función $h(n)$ que estima el costo desde un nodo actual hasta 
# la meta.

# Cómo funciona la Búsqueda Heurística Voraz:
# Es un algoritmo "codicioso": en cada paso, elige el nodo que parece estar más cerca de la meta 
# según la heurística, sin importar cuánto ha caminado ya.Utiliza una cola de prioridad 
# (simulada aquí con sort) para procesar siempre el nodo con el valor de $h(n)$ más bajo.

# Ventaja: 
# Es extremadamente rápida y suele encontrar una solución con muy pocos pasos.

# Desventaja: 
# No garantiza encontrar el camino más corto (u óptimo), ya que puede dejarse llevar por un 
# camino que parece bueno al principio pero que resulta ser más largo o un callejón sin salida.

# Mapa de intersecciones viales (Conexiones entre calles)
red_vial = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J', 'K'],
    'G': ['D', 'L'],
    'H': ['D'],
    'I': ['E', 'M', 'N'],
    'J': ['F'],
    'K': ['F', 'O'],
    'L': ['G', 'P'],
    'M': ['I'],
    'N': ['I', 'Q'],
    'O': ['K'],
    'P': ['L'],
    'Q': ['N', 'R'],
    'R': ['Q']
}

# Estimación de distancia aérea (Heurística) hasta el Hospital 'Q'
distancia_estimada_hospital = {
    'Q': 0,   # Destino alcanzado
    'N': 1, 'R': 1, 
    'I': 2, 
    'E': 3, 'M': 3, 
    'B': 4, 
    'A': 5, 'D': 5, 
    'C': 6, 'G': 6, 'H': 6, 
    'F': 7, 'L': 7, 
    'J': 8, 'K': 8, 'P': 8, 
    'O': 9
}

def navegador_emergencia_voraz(mapa, radar_h, salida, destino):
    """
    Algoritmo Greedy Search: Prioriza siempre el nodo con menor valor en el radar.
    """
    print(f"--- Iniciando Navegación de Emergencia (Origen: {salida}, Destino: {destino}) ---")
    
    # Lista de prioridad: (valor_sensor, ubicacion, ruta_seguida)
    lista_prioridad = [(radar_h[salida], salida, [salida])]
    
    # Registro de calles ya transitadas
    calles_bloqueadas = set()

    while lista_prioridad:
        # Reordenamos la lista para que el punto con 'menor distancia estimada' esté al inicio
        lista_prioridad.sort(key=lambda punto: punto[0])
        
        # Seleccionamos la ubicación más prometedora según el radar
        lectura_h, punto_actual, rastro = lista_prioridad.pop(0)
        
        print(f"Transitando por: {punto_actual} (Distancia estimada al objetivo: {lectura_h})")

        # Verificamos si el vehículo llegó al hospital
        if punto_actual == destino:
            print(f"\n¡DESTINO ALCANZADO! El equipo de emergencia llegó a '{destino}'.")
            print(f"Trayectoria completada: {' -> '.join(rastro)}")
            return True

        # Si el punto es nuevo, lo exploramos para ver sus conexiones
        if punto_actual not in calles_bloqueadas:
            calles_bloqueadas.add(punto_actual)
            
            # Revisamos las calles adyacentes
            adyacentes = mapa.get(punto_actual, [])
            for proxima in adyacentes:
                if proxima not in calles_bloqueadas:
                    # Consultamos el sensor de proximidad (heurística)
                    # Si no hay datos del sensor para una calle, asumimos que está muy lejos (infinito)
                    valor_proxima = radar_h.get(proxima, float('inf'))
                    
                    # Añadimos a la lista de prioridad para decidir el siguiente movimiento
                    lista_prioridad.append((valor_proxima, proxima, rastro + [proxima]))
                    
    print(f"\nAlerta: No se pudo establecer una ruta hacia el hospital '{destino}'.")
    return False

# --- PRUEBA DEL NAVEGADOR ---
navegador_emergencia_voraz(red_vial, distancia_estimada_hospital, salida='A', destino='K')