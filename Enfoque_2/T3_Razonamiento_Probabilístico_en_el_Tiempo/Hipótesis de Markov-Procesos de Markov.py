#¿Qué es la Hipótesis de Markov?
# La esencia de Markov se resume en una frase: "El futuro es independiente del pasado, dado el 
# presente".Imagina que estás jugando a un juego de mesa. Para saber a qué casilla te moverás, solo 
# necesitas saber en qué casilla estás ahora y qué sale en el dado. No importa si hace tres turnos 
# estabas en la salida o en la cárcel; esa información es irrelevante para tu siguiente movimiento.
# Un proceso que cumple esto se llama Proceso de Markov de Primer Orden:
# $$P(S_{t+1} | S_t, S_{t-1}, \dots, S_0) = P(S_{t+1} | S_t)$$

import random

# --- 1. DEFINICIÓN DEL MODELO ---
# Definimos los estados posibles
estados = ["Feliz", "Neutral", "Triste"]

# Matriz de Transición: Probabilidades de pasar de un estado a otro
# Formato: { estado_actual: { estado_siguiente: probabilidad } }
matriz_transicion = {
    "Feliz":  {"Feliz": 0.6, "Neutral": 0.3, "Triste": 0.1},
    "Neutral": {"Feliz": 0.3, "Neutral": 0.4, "Triste": 0.3},
    "Triste":  {"Feliz": 0.1, "Neutral": 0.4, "Triste": 0.5}
}

# --- 2. EL MOTOR DE MARKOV ---

def simular_cadena_markov(estado_inicial, pasos=10):
    """Genera una secuencia de estados basada solo en el estado anterior."""
    historial = [estado_inicial]
    estado_actual = estado_inicial
    
    print(f"[*] Iniciando simulación desde estado: {estado_inicial}")
    
    for _ in range(pasos):
        # La Hipótesis de Markov: Solo miramos 'estado_actual'
        opciones = list(matriz_transicion[estado_actual].keys())
        probabilidades = list(matriz_transicion[estado_actual].values())
        
        # Elegimos el siguiente estado basado en las probabilidades
        siguiente_estado = random.choices(opciones, weights=probabilidades)[0]
        
        historial.append(siguiente_estado)
        estado_actual = siguiente_estado
        
    return historial

# --- 3. EJECUCIÓN Y RESULTADOS ---

# Simulamos 24 horas de "vida" de la IA
bitacora_ia = simular_cadena_markov(estado_inicial="Feliz", pasos=24)

print("\n--- BITÁCORA DE ESTADOS (24 Horas) ---")
print(" -> ".join(bitacora_ia))

# Conteo de permanencia
print("\n--- ANÁLISIS DE TIEMPO ---")
for e in estados:
    print(f"Tiempo en estado {e}: {bitacora_ia.count(e)} horas")
    