'''
Aprendizaje Bayesiano:
Actualización de creencias con distribución Beta-Bernoulli
'''

import random

# ====================== PARÁMETROS =====================================

# Prior Beta(α, β)
alpha = 1   # éxitos iniciales
beta = 1    # fracasos iniciales

# Datos observados (1 = éxito, 0 = fracaso)
datos = [1, 0, 1, 1, 0, 1, 1]

# ====================== ACTUALIZACIÓN BAYESIANA ========================

def actualizar_bayes(alpha, beta, datos):
    historial = []

    for i, d in enumerate(datos):
        if d == 1:
            alpha += 1
        else:
            beta += 1

        # Estimación de probabilidad
        prob = alpha / (alpha + beta)

        historial.append((i, alpha, beta, prob))

    return historial

# ====================== EJECUCIÓN ======================================

resultado = actualizar_bayes(alpha, beta, datos)

print("\n[Aprendizaje Bayesiano]")

for paso, a, b, p in resultado:
    print(f"\nPaso {paso}:")
    print(f"Alpha (éxitos): {a}")
    print(f"Beta (fracasos): {b}")
    print(f"Probabilidad estimada: {p:.4f}")