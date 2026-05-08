#¿Qué es la Búsqueda Voraz Primero el Mejor?
# Es un algoritmo de búsqueda informada que utiliza una función de evaluación 
# $f(n) = h(n)$, donde $h(n)$ es la heurística. A diferencia de otros algoritmos que consideran 
# el costo ya recorrido, este algoritmo es "miope": solo le importa qué tan cerca parece 
# estar el objetivo desde su posición actual.

# Cómo funciona:
# Utiliza una Cola de Prioridad para expandir siempre el nodo que tiene el valor heurístico 
# más bajo.
# En cada paso, elige el camino que ofrece la mayor ganancia inmediata hacia 
# el objetivo.
# Es altamente eficiente en términos de tiempo si la heurística es buena, pero puede 
# ser subóptimo (no encontrar el camino más corto real).

# Mapa de túneles y cámaras mineras
sistema_minero = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B', 'G', 'H'], 'E': ['B', 'I'], 'F': ['C', 'J', 'K'],
    'G': ['D', 'L'], 'H': ['D'], 'I': ['E', 'M', 'N'],
    'J': ['F'], 'K': ['F', 'O'], 'L': ['G', 'P'],
    'M': ['I'], 'N': ['I', 'Q'], 'O': ['K'],
    'P': ['L'], 'Q': ['N', 'R'], 'R': ['Q']
}

# Lecturas del sensor de proximidad (Heurística) hacia la Veta Maestra 'Q'
sensor_proximidad = {
    'Q': 0, 'N': 1, 'R': 1, 'I': 2, 'E': 3, 'M': 3, 
    'B': 4, 'A': 5, 'D': 5, 'C': 6, 'G': 6, 'H': 6, 
    'F': 7, 'L': 7, 'J': 8, 'K': 8, 'P': 8, 'O': 9
}

def localizar_veta_maestra(yacimiento, sensor, punto_entrada, veta_objetivo):
    """
    Algoritmo Greedy Best-First: Prioriza la búsqueda basándose en la intensidad del sensor.
    """
    print(f"--- Iniciando Escaneo de Prospección (Origen: {punto_entrada}, Objetivo: {veta_objetivo}) ---")
    
    # Lista de prospección: (lectura_sensor, cámara_actual, registro_pasos)
    # En este modelo f(n) = h(n)
    prospectos_pendientes = [(sensor[punto_entrada], punto_entrada, [punto_entrada])]
    
    # Registro de cámaras ya excavadas o analizadas
    camaras_analizadas = set()

    while prospectos_pendientes:
        # Ordenamos los prospectos para extraer el que tiene la lectura de sensor más baja
        prospectos_pendientes.sort(key=lambda x: x[0])
        
        # Extraemos la cámara con la mejor señal de proximidad
        señal_h, camara_focal, historial = prospectos_pendientes.pop(0)
        
        print(f"Sondeando cámara: {camara_focal} (Intensidad de señal h(n): {señal_h})")

        # Comprobamos si hemos llegado a la veta maestra
        if camara_focal == veta_objetivo:
            print(f"\n¡YACIMIENTO ENCONTRADO! La veta '{veta_objetivo}' ha sido localizada.")
            print(f"Ruta de excavación recomendada: {' -> '.join(historial)}")
            return True

        # Si la cámara no ha sido analizada, expandimos la búsqueda a túneles conectados
        if camara_focal not in camaras_analizadas:
            camaras_analizadas.add(camara_focal)
            
            # Revisamos las galerías conectadas
            galerias = yacimiento.get(camara_focal, [])
            for galeria in galerias:
                if galeria not in camaras_analizadas:
                    # Obtenemos la lectura del sensor para la nueva galería
                    # Si no hay datos, asignamos una señal nula (infinito)
                    señal_galeria = sensor.get(galeria, float('inf'))
                    prospectos_pendientes.append((señal_galeria, galeria, historial + [galeria]))
                    
    print(f"\nLa veta '{veta_objetivo}' no pudo ser localizada en este sector.")
    return False

# --- EJECUCIÓN DEL PROTOCOLO MINERO ---
localizar_veta_maestra(sistema_minero, sensor_proximidad, punto_entrada='A', veta_objetivo='L')