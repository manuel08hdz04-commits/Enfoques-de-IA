#¿Qué es la Búsqueda de Haz Local (Beam Search)?
# Es una variante de la búsqueda por anchura (BFS) que utiliza una memoria limitada. En lugar de 
# explorar todas las posibilidades de un nivel, el algoritmo solo conserva las k mejores opciones 
# (el ancho del haz).

# Cómo funciona:
# Ancho del Haz (k): Es el número máximo de estados que el algoritmo mantiene en la "frontera" en cada 
# nivel.
# Poda Selectiva: Al final de cada nivel, se evalúan todos los sucesores, pero se descartan los 
# peores, manteniendo solo los $k$ más prometedores según la heurística.
# Eficiencia: Reduce drásticamente el uso de memoria comparado con BFS, aunque a riesgo de descartar 
# el camino óptimo si este no parece bueno al principio.

# Mapa de sectores aéreos
red_sectores = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Radar de proximidad (Heurística): Distancia estimada al Objetivo 'F'
radar_objetivo = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def despliegue_escuadron_haz(punto_inicio, objetivo_final, ancho_haz=2):
    """
    Simula una búsqueda de haz donde solo sobreviven los 'k' mejores drones por nivel.
    """
    # La frontera representa el grupo de drones activos en el nivel actual
    escuadron_activo = [punto_inicio]
    altitud_busqueda = 0

    print(f"--- Iniciando Barrido con Haz (Ancho k={ancho_haz}) ---")

    while escuadron_activo:
        print(f"Zona de Escaneo {altitud_busqueda}: {escuadron_activo}")

        # Verificamos si algún dron del escuadrón detectó el objetivo
        if objetivo_final in escuadron_activo:
            print(f"¡OBJETIVO DETECTADO! El escuadrón alcanzó el sector '{objetivo_final}'.")
            return True

        # Generamos los posibles sectores para el siguiente nivel de vuelo
        potenciales_sectores = []
        for dron_posicion in escuadron_activo:
            potenciales_sectores.extend(red_sectores.get(dron_posicion, []))

        # PODA DE HAZ: Ordenamos por radar y mantenemos solo los 'k' mejores
        # Los drones que se dirigen a zonas con heurística alta son desactivados.
        escuadron_activo = sorted(
            list(set(potenciales_sectores)), # Eliminamos duplicados
            key=lambda x: radar_objetivo.get(x, float('inf'))
        )[:ancho_haz]

        altitud_busqueda += 1

    print("--- El escuadrón perdió la señal. Objetivo no localizado ---")
    return False

# --- LANZAMIENTO DEL ESCUADRÓN ---
despliegue_escuadron_haz('A', 'F', ancho_haz=2)