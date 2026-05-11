'''
Filtro de Kalman (1D):
Estimación de una variable (posición) combinando predicción y medición con ruido
'''

# ====================== PARÁMETROS =====================================

# Estado inicial (posición estimada)
x = 0  

# Incertidumbre inicial
P = 1  

# Ruido del proceso (qué tanto cambia el sistema)
Q = 0.1  

# Ruido de medición (qué tan confiable es el sensor)
R = 0.5  

# ====================== MEDICIONES =====================================

# Mediciones simuladas (con ruido)
mediciones = [1, 2, 3, 2.5, 2.8]

# ====================== RECORRIDO ======================================

def imprimir_estado(k, x, P, K):
    print(f"\nPaso {k}:")
    print(f"Estimación (x): {x:.4f}")
    print(f"Incertidumbre (P): {P:.4f}")
    print(f"Ganancia de Kalman (K): {K:.4f}")

# ====================== FILTRO DE KALMAN ===============================

def filtro_kalman(mediciones):
    global x, P

    for k, z in enumerate(mediciones):

        # 🔹 1. PREDICCIÓN
        x_pred = x            # Modelo simple (no cambia)
        P_pred = P + Q        # Aumenta incertidumbre

        # 🔹 2. ACTUALIZACIÓN (CORRECCIÓN)
        K = P_pred / (P_pred + R)         # Ganancia de Kalman
        x = x_pred + K * (z - x_pred)     # Nueva estimación
        P = (1 - K) * P_pred              # Nueva incertidumbre

        imprimir_estado(k, x, P, K)

# ====================== EJECUCIÓN ======================================

filtro_kalman(mediciones)
