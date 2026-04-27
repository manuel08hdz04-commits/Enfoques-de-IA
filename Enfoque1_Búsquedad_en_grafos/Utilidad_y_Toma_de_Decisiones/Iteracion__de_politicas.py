'''
ITERACIÓN DE POLÍTICAS

El robot decide qué hacer en cada lugar
para maximizar su ganancia a largo plazo.
'''

# ====================== ALGORITMO ======================================

def iteracion_politicas(estados, acciones, transiciones, recompensas, gamma=0.9):
    politica = {s: acciones[0] for s in estados}
    V = {s: 0 for s in estados}

    estable = False

    while not estable:

        # 🔹 Evaluar política actual
        for _ in range(10):
            for s in estados:
                a = politica[s]
                V[s] = sum(
                    transiciones[s][a][s2] *
                    (recompensas[s][a][s2] + gamma * V[s2])
                    for s2 in estados
                )

        # 🔹 Mejorar política
        estable = True
        for s in estados:
            mejor = max(
                acciones,
                key=lambda a: sum(
                    transiciones[s][a][s2] *
                    (recompensas[s][a][s2] + gamma * V[s2])
                    for s2 in estados
                )
            )

            if mejor != politica[s]:
                politica[s] = mejor
                estable = False

    return politica


# ====================== EJEMPLO CLARO ==================================

estados = ["Casa", "Trabajo"]
acciones = ["quedarse", "ir"]

transiciones = {
    "Casa": {
        "quedarse": {"Casa": 1.0, "Trabajo": 0.0},
        "ir": {"Casa": 0.2, "Trabajo": 0.8}
    },
    "Trabajo": {
        "quedarse": {"Trabajo": 1.0, "Casa": 0.0},
        "ir": {"Trabajo": 0.3, "Casa": 0.7}
    }
}

recompensas = {
    "Casa": {
        "quedarse": {"Casa": 1, "Trabajo": 0},   # descanso
        "ir": {"Casa": 0, "Trabajo": 5}         # ir a trabajar
    },
    "Trabajo": {
        "quedarse": {"Trabajo": 6, "Casa": 0},  # gana dinero
        "ir": {"Trabajo": 0, "Casa": 2}         # regresar
    }
}


# ====================== EJECUCIÓN ======================================

print("\n[28 - Política óptima]")
resultado = iteracion_politicas(estados, acciones, transiciones, recompensas)

for estado in resultado:
    print(f"En {estado} → hacer: {resultado[estado]}")
