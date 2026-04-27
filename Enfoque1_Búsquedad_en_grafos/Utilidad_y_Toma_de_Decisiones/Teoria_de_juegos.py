'''
TEORÍA DE JUEGOS - EQUILIBRIO DE NASH

Ningún jugador mejora cambiando su estrategia solo.
Cada quien está tomando su mejor decisión dado lo que hace el otro
Ejemplo: dos empresas fijando precios.
'''

# ====================== EQUILIBRIO =====================================

def equilibrio_nash(matriz):
    eq = []
    filas = len(matriz)
    cols = len(matriz[0])

    for i in range(filas):
        for j in range(cols):

            # Mejor en fila
            mejor_fila = max(matriz[i])

            # Mejor en columna
            mejor_col = max(matriz[k][j] for k in range(filas))

            if matriz[i][j] == mejor_fila and matriz[i][j] == mejor_col:
                eq.append((i, j))

    return eq


# ====================== EJEMPLO ========================================

# Pagos de empresa A
matriz = [
    [3, 1],
    [2, 4]
]

print("\n[32 - Nash]")
print("Equilibrios:", equilibrio_nash(matriz))
