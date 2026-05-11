#Las 4 Operaciones del Tiempo
#Filtrado (Filtering): Estimar el estado actual dado todo el historial hasta hoy. Es lo que hace tu 
# teléfono para saber dónde estás exactamente en el mapa a pesar del error del GPS.

#Predicción (Prediction): Estimar un estado futuro basado en lo que sabemos hoy. Útil para evitar 
# colisiones.

#Suavizado (Smoothing): Re-estimar el pasado. Miramos el historial completo para corregir lo que 
# creíamos que pasó en el paso 5 ahora que ya estamos en el paso 10. Da una visión más nítida de la 
# trayectoria.

#Explicación (Most Likely Explanation): Encontrar la secuencia de estados más probable que generó 
# las observaciones. No solo punto por punto, sino el "camino" completo más lógico.

import random

# --- 1. CONFIGURACIÓN DEL MODELO ---
# Probabilidades de transición (Movimiento)
p_moverse = 0.8  # Probabilidad de avanzar a la siguiente posición
p_quedarse = 0.2

# Probabilidades de observación (Sensor con ruido)
# Si estoy en X, ¿qué tan probable es que el sensor diga X?
p_sensor_correcto = 0.7
p_sensor_error = 0.15 # (a la izquierda o derecha)

def sensor_verosimilitud(pos_real, pos_observada):
    if pos_real == pos_observada: return p_sensor_correcto
    if abs(pos_real - pos_observada) == 1: return p_sensor_error
    return 0.01

# --- 2. OPERACIONES TEMPORALES ---

def filtrar(prob_anterior, observacion_actual, num_estados):
    """FILTRADO: Estima el 'AHORA'"""
    nueva_estimacion = [0.0] * num_estados
    
    for s_actual in range(num_estados):
        # Predicción un paso adelante (Prior)
        prior = 0.0
        for s_prev in range(num_estados):
            # Probabilidad de haber venido del estado anterior
            transicion = p_moverse if s_actual == s_prev + 1 else (p_quedarse if s_actual == s_prev else 0.0)
            prior += prob_anterior[s_prev] * transicion
            
        # Actualización con la observación (Posterior)
        nueva_estimacion[s_actual] = prior * sensor_verosimilitud(s_actual, observacion_actual)
    
    # Normalizar
    total = sum(nueva_estimacion)
    return [p / total for p in nueva_estimacion]

def predecir(prob_actual, pasos, num_estados):
    """PREDICCIÓN: Estima el 'FUTURO'"""
    pred = list(prob_actual)
    for _ in range(pasos):
        nueva_pred = [0.0] * num_estados
        for s_next in range(num_estados):
            for s_curr in range(num_estados):
                trans = p_moverse if s_next == s_curr + 1 else (p_quedarse if s_next == s_curr else 0.0)
                nueva_pred[s_next] += pred[s_curr] * trans
        pred = nueva_pred
    return pred

# --- 3. SIMULACIÓN ---
num_estados = 10
historial_observaciones = [0, 1, 2, 2, 4] # El sensor falló en el tiempo 3 (marcó 2 de nuevo)

# Iniciamos con certeza en posición 0
estado_creido = [1.0] + [0.0]*(num_estados-1)

print("--- INFERENCIA TEMPORAL ---")
for t, obs in enumerate(historial_observaciones):
    estado_creido = filtrar(estado_creido, obs, num_estados)
    pos_probable = estado_creido.index(max(estado_creido))
    print(f"Tiempo {t} | Sensor dice: {obs} | IA cree estar en: {pos_probable} (Confianza: {max(estado_creido):.2%})")

# Predicción a futuro
futuro = predecir(estado_creido, 2, num_estados)
print(f"\nPredicción a +2 pasos: Posición más probable {futuro.index(max(futuro))}")