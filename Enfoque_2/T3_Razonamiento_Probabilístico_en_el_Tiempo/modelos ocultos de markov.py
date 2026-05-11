'''
HMM
Modelo probabilístico que calcula qué tan probable es una secuencia de observaciones
dada una serie de estados ocultos.

que tan probable es una secuencia de observaciones
'''

# ====================== MODELO HMM =====================================

ESTADOS = ['Lluvioso', 'Soleado']
OBSERVACIONES = ['caminar', 'comprar', 'limpiar']

# Probabilidades iniciales
PI = {
    'Lluvioso': 0.6,
    'Soleado': 0.4
}

# Probabilidades de transición (cambio de un estado a otro)
TRANSICION = {
    'Lluvioso': {'Lluvioso': 0.7, 'Soleado': 0.3}, # Si el estado actual es lluvioso, hay 0.7 de probabilidad de permanecer en lluvioso
    'Soleado': {'Lluvioso': 0.4, 'Soleado': 0.6}
}

# Probabilidades de emisión (lo que observo)
EMISION = {
    'Lluvioso': {'caminar': 0.1, 'comprar': 0.4, 'limpiar': 0.5}, #si llueve, es mas probable que limpie a que camine
    'Soleado': {'caminar': 0.6, 'comprar': 0.3, 'limpiar': 0.1}   #si esta soleado, es mas probable que camine
}

# ====================== RECORRIDO ======================================

def imprimir_tabla(alpha):
    print("\n[HMM - Forward] Probabilidades:")
    for t, paso in enumerate(alpha):
        print(f"Tiempo {t}: {paso}")

# ====================== ALGORITMO FORWARD ==============================

def hmm_forward(secuencia):
    alpha = []

    # 🔹 Paso 1: inicialización
    alpha_0 = {}
    for estado in ESTADOS:
        alpha_0[estado] = PI[estado] * EMISION[estado][secuencia[0]]
    alpha.append(alpha_0)

    # 🔹 Paso 2: recursión
    for t in range(1, len(secuencia)):
        alpha_t = {}
        for estado_actual in ESTADOS:
            suma = 0
            for estado_prev in ESTADOS:
                suma += alpha[t-1][estado_prev] * TRANSICION[estado_prev][estado_actual]
            alpha_t[estado_actual] = suma * EMISION[estado_actual][secuencia[t]]
        alpha.append(alpha_t)

    # 🔹 Paso 3: terminación
    prob_total = sum(alpha[-1].values())

    imprimir_tabla(alpha)
    print("\nProbabilidad total de la secuencia:", prob_total)

# ====================== EJECUCIÓN ======================================

secuencia = ['caminar', 'comprar', 'limpiar'] #que probabilidad hay de realizar esta secuencia
hmm_forward(secuencia)