#¿Qué es la Búsqueda A*?
# El algoritmo A* es una búsqueda informada que destaca por ser completa y óptima. Combina las 
# ventajas de la Búsqueda de Costo Uniforme (que mira hacia atrás) y la Búsqueda Voraz (que mira 
# hacia adelante).

# Cómo funciona:
# Utiliza una función de evaluación compuesta:$$f(n) = g(n) + h(n)$$
# g(n)$: El costo real acumulado desde el origen hasta el nodo actual.
# h(n)$: El costo estimado (heurística) desde el nodo actual hasta la meta.
# f(n)$: El costo total estimado del camino más barato que pasa por $n$.
# Al elegir siempre el nodo con el valor $f(n)$ más bajo, A* evita explorar caminos costosos y se 
# dirige directamente hacia el objetivo, garantizando el camino más corto siempre que la heurística 
# sea admisible (que nunca sobreestime el costo real).

# Mapa de conexiones logísticas (Red de distribución)
red_distribucion = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B', 'G', 'H'], 'E': ['B', 'I'], 'F': ['C', 'J', 'K'],
    'G': ['D', 'L'], 'H': ['D'], 'I': ['E', 'M', 'N'],
    'J': ['F'], 'K': ['F', 'O'], 'L': ['G', 'P'],
    'M': ['I'], 'N': ['I', 'Q'], 'O': ['K'],
    'P': ['L'], 'Q': ['N', 'R'], 'R': ['Q']
}

# Estimador de proximidad (Heurística h) hacia el Centro de Distribución 'Q'
estimacion_proximidad = {
    'Q': 0, 'N': 1, 'R': 1, 'I': 2, 'E': 3, 'M': 3, 
    'B': 4, 'A': 5, 'D': 5, 'C': 6, 'G': 6, 'H': 6, 
    'F': 7, 'L': 7, 'J': 8, 'K': 8, 'P': 8, 'O': 9
}

def optimizador_ruta_a_estrella(mapa, sensor_h, punto_partida, punto_entrega):
    """
    Algoritmo A*: Calcula la trayectoria óptima equilibrando gasto real y estimación.
    """
    print(f"--- Sistema de Navegación Autónomo (Ruta: {punto_partida} a {punto_entrega}) ---")
    
    # Iniciamos valores del punto de origen
    g_acumulado = 0
    f_total = g_acumulado + sensor_h[punto_partida]
    
    # Registro de despacho: (f_prioridad, g_real, punto_actual, historial_ruta)
    plan_viaje = [(f_total, g_acumulado, punto_partida, [punto_partida])]
    
    # Memoria de sectores ya validados
    sectores_optimizados = set()

    while plan_viaje:
        # El sistema selecciona el trayecto con el menor costo total proyectado (f)
        plan_viaje.sort(key=lambda x: x[0])
        
        costo_f, costo_g, ubicacion, trayectoria = plan_viaje.pop(0)
        
        print(f"Validando sector: {ubicacion} (Inversión g: {costo_g} | Proyección f: {costo_f})")

        # Verificación de llegada al punto de entrega
        if ubicacion == punto_entrega:
            print(f"\n¡ENTREGA EXITOSA! Trayectoria óptima confirmada.")
            print(f"Hoja de ruta: {' -> '.join(trayectoria)}")
            print(f"Costo operativo total: {costo_g}")
            return True

        # Si el sector no ha sido procesado, expandimos los puntos colindantes
        if ubicacion not in sectores_optimizados:
            sectores_optimizados.add(ubicacion)
            
            vecindad = mapa.get(ubicacion, [])
            for punto_adyacente in vecindad:
                if punto_adyacente not in sectores_optimizados:
                    # Cálculo de costos para el siguiente paso (cada tramo vale 1)
                    nuevo_g = costo_g + 1
                    valor_h = sensor_h.get(punto_adyacente, float('inf'))
                    nuevo_f = nuevo_g + valor_h
                    
                    # Actualizamos el plan de viaje con la nueva ramificación
                    plan_viaje.append((nuevo_f, nuevo_g, punto_adyacente, trayectoria + [punto_adyacente]))
                    
    print(f"\nNo se encontró una ruta viable hacia el destino: {punto_entrega}")
    return False

# --- EJECUCIÓN DEL NAVEGADOR ---
optimizador_ruta_a_estrella(red_distribucion, estimacion_proximidad, punto_partida='A', punto_entrega='R')