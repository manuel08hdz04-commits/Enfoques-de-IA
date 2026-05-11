'''
Algoritmo EM (Expectation-Maximization)
Clustering probabilístico con mezcla de gaussianas (simplificado)
'''

import math

# ====================== DATOS ==========================================

datos = [1, 2, 1.5, 8, 9, 8.5]

# ====================== PARÁMETROS INICIALES ===========================

# Medias iniciales (dos clusters)
mu1 = 2
mu2 = 8

# Varianza (fija para simplificar)
sigma = 1

# Pesos (probabilidad de cada cluster)
pi1 = 0.5
pi2 = 0.5

# ====================== FUNCIONES ======================================

def gauss(x, mu, sigma):
    return (1 / math.sqrt(2 * math.pi * sigma**2)) * math.exp(-((x - mu)**2) / (2 * sigma**2))

# ====================== EM =============================================

def em(datos, iteraciones=5):
    global mu1, mu2, pi1, pi2

    for it in range(iteraciones):

        # 🔹 E-step (responsabilidades)
        responsabilidades = []

        for x in datos:
            p1 = pi1 * gauss(x, mu1, sigma)
            p2 = pi2 * gauss(x, mu2, sigma)

            total = p1 + p2

            r1 = p1 / total
            r2 = p2 / total

            responsabilidades.append((r1, r2))

        # 🔹 M-step (actualización)
        sum_r1 = sum(r[0] for r in responsabilidades)
        sum_r2 = sum(r[1] for r in responsabilidades)

        mu1 = sum(r[0] * x for r, x in zip(responsabilidades, datos)) / sum_r1
        mu2 = sum(r[1] * x for r, x in zip(responsabilidades, datos)) / sum_r2

        pi1 = sum_r1 / len(datos)
        pi2 = sum_r2 / len(datos)

        # 🔹 Mostrar resultados
        print(f"\nIteración {it + 1}:")
        print(f"mu1 = {mu1:.3f}, mu2 = {mu2:.3f}")
        print(f"pi1 = {pi1:.3f}, pi2 = {pi2:.3f}")

# ====================== EJECUCIÓN ======================================

em(datos)