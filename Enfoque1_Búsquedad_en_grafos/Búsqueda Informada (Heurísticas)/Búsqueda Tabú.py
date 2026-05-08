#¿Qué es la Búsqueda Tabú?
#La Búsqueda Tabú es una metaheurística de optimización local que mejora el rendimiento de otros 
# algoritmos (como la Ascensión de Colinas) al utilizar una memoria de corto plazo.

#Cómo funciona:
# Lista Tabú: Es el corazón del algoritmo. Es un registro de los estados o movimientos realizados 
# recientemente que están "prohibidos" (tabú) durante un número determinado de iteraciones.
# Evasión de Ciclos: Al prohibir el regreso a nodos visitados recientemente, el algoritmo obliga a 
# la exploración de nuevas áreas del grafo, evitando que se quede atrapado en bucles infinitos o 
# máximos locales mediocres.
# Criterio de Aspiración: (Aunque no está en este código básico) En versiones avanzadas, se puede 
# ignorar el estado "tabú" si un movimiento es tan bueno que garantiza encontrar el objetivo.

# Mapa de sectores de la zona de exclusión
sectores_mapa = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Radar de proximidad (HEURISTICA): Estimación de distancia a la Salida 'F'
radar_distancia = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# --- UTILIDAD DE TELEMETRÍA ---
def reporte_mision(ruta, sistema):
    """Muestra el rastro dejado por el explorador."""
    print(f"\n[Protocolo {sistema}] Bitácora de movimiento:")
    for paso, sector in enumerate(ruta):
        print(f"Instante {paso}: Sector {sector}")

# --- BÚSQUEDA TABÚ ---
def protocolo_exploracion_tabu(inicio, salida_emergencia, iteraciones_max=10):
    """
    Simula una búsqueda que bloquea sectores visitados para evitar ciclos.
    """
    ubicacion_actual = inicio
    # Lista Tabú: Memoria de sectores prohibidos para evitar retrocesos
    zonas_restringidas = []
    rastro_gps = [ubicacion_actual]

    for i in range(iteraciones_max):
        # Verificamos si el explorador alcanzó la salida
        if ubicacion_actual == salida_emergencia:
            reporte_mision(rastro_gps, "TABÚ")
            print(f"--- ÉXITO: Salida '{salida_emergencia}' localizada ---")
            return

        # Escaneamos los sectores vecinos
        vecinos_detectados = sectores_mapa.get(ubicacion_actual, [])
        
        # FILTRO TABÚ: Solo consideramos sectores que NO estén en la lista prohibida
        candidatos_viables = [nodo for nodo in vecinos_detectados if nodo not in zonas_restringidas]

        # Si no hay opciones fuera de la lista tabú, el explorador se detiene
        if not candidatos_viables:
            print(f"Alerta: Sin movimientos legales en el paso {i}. Perímetro bloqueado.")
            break

        # Selección inteligente: Elegimos el sector con la menor distancia en el radar
        proximo_sector = min(candidatos_viables, key=lambda x: radar_distancia[x])
        
        # Marcamos la ubicación actual como "TABÚ" (Prohibida)
        zonas_restringidas.append(ubicacion_actual)
        
        # Actualizamos la posición y el historial
        ubicacion_actual = proximo_sector
        rastro_gps.append(ubicacion_actual)

    reporte_mision(rastro_gps, "TABÚ")
    print(f"Estado final del explorador: Sector {ubicacion_actual}")

# --- EJECUCIÓN DEL PROTOCOLO ---
protocolo_exploracion_tabu('A', 'F')