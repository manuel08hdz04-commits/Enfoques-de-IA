'''
APRENDIZAJE POR REFUERZO PASIVO

El agente NO elige acciones,
solo aprende el valor de los estados.

Usa retornos acumulados (Monte Carlo).
Este algorritmo busca aprender que estados son mejores sin cambiar la política. "Cual es el valor del que se obtiene mayor recompensa"
'''

# ====================== ALGORITMO ======================================

def refuerzo_pasivo(episodios, gamma=0.9):
    V = {}
    conteo = {}

    for episodio in episodios:
        G = 0

        # 🔹 Recorrer episodio en reversa
        for estado, recompensa in reversed(episodio):
            G = recompensa + gamma * G

            if estado not in V:
                V[estado] = 0
                conteo[estado] = 0

            conteo[estado] += 1

            # Promedio incremental
            V[estado] += (G - V[estado]) / conteo[estado]

    return V


# ====================== EJEMPLO ========================================

episodios = [
    [("Casa", 5), ("Trabajo", 10)],
    [("Casa", 3), ("Trabajo", 8)]
]

print("\nRefuerzo Pasivo:")
print(refuerzo_pasivo(episodios))
