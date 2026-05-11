'''
k-means desde cero
'''

import random
import math

datos = [(1,2), (2,3), (3,3), (6,5), (7,7)]

k = 2

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Inicializar centroides aleatorios
centroides = random.sample(datos, k)

for _ in range(10):
    clusters = {i: [] for i in range(k)}

    # Asignar puntos
    for punto in datos:
        distancias = [distancia(punto, c) for c in centroides]
        idx = distancias.index(min(distancias))
        clusters[idx].append(punto)

    # Recalcular centroides
    nuevos = []
    for i in clusters:
        xs = [p[0] for p in clusters[i]]
        ys = [p[1] for p in clusters[i]]
        nuevos.append((sum(xs)/len(xs), sum(ys)/len(ys)))

    centroides = nuevos

print("Centroides:", centroides)
print("Clusters:", clusters)