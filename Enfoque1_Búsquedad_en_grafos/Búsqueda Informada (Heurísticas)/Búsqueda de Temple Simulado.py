#¿Qué es el Temple Simulado?
# El Temple Simulado es una metaheurística inspirada en el proceso físico de enfriamiento de los 
# metales. A diferencia de la Ascensión de Colinas (que es rígida y se queda atrapada en picos falsos), 
# este algoritmo permite "errores" estratégicos al principio.

# Cómo funciona:
# Temperatura ($T$): Representa la probabilidad de aceptar un camino peor. Cuando el metal está 
# "caliente", el algoritmo es caótico y explora opciones malas para evitar quedarse atrapado.
# Enfriamiento: Conforme el tiempo pasa (la temperatura baja), el algoritmo se vuelve más selectivo y 
# "duro", aceptando solo movimientos que realmente mejoren su posición.
# Probabilidad de Boltzmann: Se usa la fórmula $P = e^{-\Delta/T}$ para decidir si aceptamos un paso 
# atrás. Si la temperatura es alta, $P$ es grande. Si es baja, $P$ tiende a cero.

import random
import math

# Mapa de estados moleculares (Conexiones entre fases)
red_molecular = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Energía de inestabilidad (Heurística): Buscamos llegar a la energía 0 (Estado Estable 'F')
energia_nodo = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def reporte_de_forja(historia, tecnica):
    """Muestra la evolución del material durante el proceso."""
    print(f"\n[{tecnica}] Evolución del material:")
    for paso, estado in enumerate(historia):
        print(f"Etapa {paso}: Fase {estado}")

def proceso_temple_simulado(punto_partida, estado_meta, calor_inicial=10):
    """
    Simula el enfriamiento de un metal para encontrar el estado de menor energía.
    """
    fase_actual = punto_partida
    bitacora_fases = [fase_actual]
    temperatura = calor_inicial

    while temperatura > 0.1:
        # Si el material alcanza el estado de estabilidad máxima
        if fase_actual == estado_meta:
            reporte_de_forja(bitacora_fases, "Temple Simulado")
            print(f"--- ÉXITO: Estado estable '{estado_meta}' alcanzado ---")
            return

        # Elegimos una dirección de cambio aleatoria (Agitación térmica)
        opciones = red_molecular.get(fase_actual, [])
        proxima_fase = random.choice(opciones) if opciones else fase_actual
        
        # Calculamos la diferencia de energía (Delta)
        # Delta negativo significa que el nuevo estado es mejor (más estable)
        delta_energia = energia_nodo[proxima_fase] - energia_nodo[fase_actual]

        # REGLA MAESTRA:
        # Si el nuevo estado es mejor (delta < 0), lo aceptamos siempre.
        # Si es peor, lo aceptamos solo si el "calor" permite la fluctuación.
        if delta_energia < 0 or random.random() < math.exp(-delta_energia / temperatura):
            fase_actual = proxima_fase
            bitacora_fases.append(fase_actual)

        # Enfriamiento progresivo del metal (Factor de reducción)
        temperatura *= 0.85

    reporte_de_forja(bitacora_fases, "Temple Simulado")
    print(f"Resultado tras enfriamiento: Fase {fase_actual}")

# --- INICIO DE LA FORJA ---
proceso_temple_simulado('A', 'F')