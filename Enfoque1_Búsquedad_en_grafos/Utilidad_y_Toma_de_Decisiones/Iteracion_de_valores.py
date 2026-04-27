'''
ITERACIÓN DE VALORES

Calcula el valor óptimo de cada estado
en un proceso de decisión.
'''

def iteracion_valores(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=20):
    V = {s: 0 for s in estados}

    for _ in range(iteraciones):
        nuevo_V = {}

        for s in estados:
            nuevo_V[s] = max(
                sum(transiciones[s][a][s2]*(recompensas[s][a][s2] + gamma*V[s2])
                    for s2 in estados)
                for a in acciones
            )

        V = nuevo_V

    return V


# EJEMPLO (robot)
estados = ["Casa","Trabajo"]
acciones = ["ir"]

transiciones = {
    "Casa":{"ir":{"Casa":0.2,"Trabajo":0.8}},
    "Trabajo":{"ir":{"Casa":0.6,"Trabajo":0.4}}
}

recompensas = {
    "Casa":{"ir":{"Casa":1,"Trabajo":5}},
    "Trabajo":{"ir":{"Casa":2,"Trabajo":3}}
}

print("\nValores esperados para cada estado:")
print(iteracion_valores(estados, acciones, transiciones, recompensas))
