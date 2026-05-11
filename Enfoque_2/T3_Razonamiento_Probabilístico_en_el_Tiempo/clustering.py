'''
Clustering jerárquico simple (aglomerativo)
'''

import math

datos = [(1,2), (2,3), (6,5), (7,7)]

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# cada punto es un cluster
clusters = [[p] for p in datos]

def distancia_clusters(c1, c2):
    return min(distancia(p1, p2) for p1 in c1 for p2 in c2)

while len(clusters) > 1:
    min_dist = float('inf')
    merge = (0, 1)

    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            d = distancia_clusters(clusters[i], clusters[j])
            if d < min_dist:
                min_dist = d
                merge = (i, j)

    i, j = merge
    clusters[i] += clusters[j]
    clusters.pop(j)

    print("Clusters:", clusters)
    