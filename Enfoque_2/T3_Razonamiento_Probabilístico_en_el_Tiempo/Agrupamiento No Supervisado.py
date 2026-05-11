'''
K-means (agrupamiento no supervisado)
Agrupa datos en K clusters
'''

import random

# ====================== DATOS ==========================================

datos = [1, 2, 1.5, 8, 9, 8.5]

# Número de clusters
K = 2

# ====================== INICIALIZACIÓN ================================

# Elegir centroides iniciales aleatorios
centroides = random.sample(datos, K)

# ====================== K-MEANS ========================================

def kmeans(datos, centroides, iteraciones=5):
    for it in range(iteraciones):

        clusters = {i: [] for i in range(K)}

        # 🔹 1. ASIGNACIÓN
        for x in datos:
            distancias = [abs(x - c) for c in centroides]
            cluster = distancias.index(min(distancias))
            clusters[cluster].append(x)

        # 🔹 2. ACTUALIZACIÓN
        nuevos_centroides = []
        for i in range(K):
            if clusters[i]:
                nuevo = sum(clusters[i]) / len(clusters[i])
            else:
                nuevo = centroides[i]
            nuevos_centroides.append(nuevo)

        centroides = nuevos_centroides

        # 🔹 Mostrar estado
        print(f"\nIteración {it+1}:")
        print("Centroides:", centroides)
        print("Clusters:", clusters)

    return centroides, clusters

# ====================== EJECUCIÓN ======================================

centroides, clusters = kmeans(datos, centroides)
