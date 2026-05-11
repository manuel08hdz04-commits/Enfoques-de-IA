'''
Red Bayesiana Dinámica + Filtro de Partículas
Estimación de estado oculto en el tiempo
'''

import random

# ====================== PARÁMETROS =====================================

NUM_PARTICULAS = 100

# Estado inicial (distribución uniforme)
particulas = [random.uniform(0, 10) for _ in range(NUM_PARTICULAS)]

# ====================== MODELOS ========================================

def transicion(x):
    """
    Modelo de transición:
    x_t = x_t-1 + movimiento + ruido
    """
    movimiento = 1
    ruido = random.gauss(0, 0.5)
    return x + movimiento + ruido

def verosimilitud(z, x):
    """
    Qué tan probable es observar z dado estado x
    """
    error = z - x
    return (2.71828 ** (- (error**2) / 2))  # gaussiana simple

# ====================== FILTRO DE PARTÍCULAS ===========================

def filtro_particulas(mediciones):
    global particulas

    for t, z in enumerate(mediciones):

        # 🔹 1. PREDICCIÓN
        particulas = [transicion(x) for x in particulas]

        # 🔹 2. PESOS (IMPORTANCIA)
        pesos = [verosimilitud(z, x) for x in particulas]

        # Normalizar pesos
        suma = sum(pesos)
        pesos = [p / suma for p in pesos]

        # 🔹 3. RESAMPLING
        nuevas_particulas = random.choices(particulas, weights=pesos, k=NUM_PARTICULAS)
        particulas = nuevas_particulas

        # 🔹 4. ESTIMACIÓN
        estimacion = sum(particulas) / NUM_PARTICULAS

        print(f"\nPaso {t}:")
        print(f"Medición: {z}")
        print(f"Estimación: {estimacion:.3f}")

# ====================== EJECUCIÓN ======================================

# Mediciones con ruido (simuladas)
mediciones = [1, 2, 3, 4, 5]

filtro_particulas(mediciones)