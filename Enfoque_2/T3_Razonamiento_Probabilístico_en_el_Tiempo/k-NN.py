'''
k-NN desde cero
'''

import math
from collections import Counter

# Datos: (x, y, clase)
datos = [
    (1, 2, 'A'),
    (2, 3, 'A'),
    (3, 3, 'B'),
    (6, 5, 'B'),
    (7, 7, 'B')
]

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def knn(punto, k=3):
    distancias = []

    for dato in datos:
        d = distancia(punto, dato)
        distancias.append((d, dato[2]))

    distancias.sort()
    vecinos = [clase for _, clase in distancias[:k]]

    return Counter(vecinos).most_common(1)[0][0]

# Ejemplo
print("Clase:", knn((4,4)))