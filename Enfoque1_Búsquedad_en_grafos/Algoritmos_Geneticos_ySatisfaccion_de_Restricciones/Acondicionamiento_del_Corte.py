from itertools import product

def acondicionamiento_corte(variables, dominios, restricciones, conjunto_corte):
    soluciones = []

    def backtracking(asignacion):
        if len(asignacion) == len(variables):
            soluciones.append(asignacion.copy())
            return

        variable = [v for v in variables if v not in asignacion][0]

        for valor in dominios[variable]:
            asignacion[variable] = valor

            if all(restriccion(asignacion) for restriccion in restricciones):
                backtracking(asignacion)

            del asignacion[variable]

    # probar combinaciones del corte
    for valores in product(*[dominios[v] for v in conjunto_corte]):
        asignacion_inicial = dict(zip(conjunto_corte, valores))
        backtracking(asignacion_inicial)

    return soluciones


# -------------------------
#EJEMPLO DE USO TIPO MAPA
# -------------------------

# Variables
variables = ["A", "B", "C"]

# Dominios (colores)
dominios = {
    "A": ["Rojo", "Verde"],
    "B": ["Rojo", "Verde"],
    "C": ["Rojo", "Verde"]
}

# Restricciones (no repetir color entre vecinos)
def restriccion_AB(asig):
    return not ("A" in asig and "B" in asig and asig["A"] == asig["B"])

def restriccion_BC(asig):
    return not ("B" in asig and "C" in asig and asig["B"] == asig["C"])

restricciones = [restriccion_AB, restriccion_BC]

# Conjunto de corte (rompe dependencia)
conjunto_corte = ["B"]

# Ejecutar algoritmo
soluciones = acondicionamiento_corte(variables, dominios, restricciones, conjunto_corte)

# Mostrar resultados
print("Soluciones encontradas:")
for sol in soluciones:
    print(sol)
