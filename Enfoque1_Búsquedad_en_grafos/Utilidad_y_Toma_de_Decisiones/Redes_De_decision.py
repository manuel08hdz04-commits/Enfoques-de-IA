'''
RED DE DECISIÓN

Modelo para elegir la mejor acción considerando incertidumbre.

Se basa en calcular el valor esperado de cada decisión:
valor esperado = probabilidad * utilidad

Permite decidir, por ejemplo:
- invertir o no
- tomar un riesgo o no
'''

# ====================== FUNCIÓN DE UTILIDAD ============================

def utilidad(estado):
    # Calcula qué tan buena es una decisión
    # utilidad = ganancia - costo
    return estado["ganancia"] - estado["costo"]


# ====================== ALGORITMO PRINCIPAL ===========================

def mejor_decision(acciones):
    mejor_accion = None
    mejor_valor = float("-inf")  # valor inicial muy bajo

    # 🔹 Evaluar cada acción posible
    for accion in acciones:
        valor_total = 0  # valor esperado de la acción

        # 🔹 Recorrer los resultados posibles
        for resultado, probabilidad in accion["resultados"]:
            # calcular contribución al valor esperado
            valor_total += probabilidad * utilidad(resultado)

        # 🔹 Comparar con la mejor opción actual
        if valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_accion = accion

    return mejor_accion


# ====================== EJEMPLO =======================================

# Decidir si invertir o no
acciones = [
    {
        "nombre": "Invertir",
        "resultados": [
            ({"ganancia": 10000, "costo": 2000}, 0.6),  # escenario bueno
            ({"ganancia": 2000, "costo": 2000}, 0.4)    # escenario malo
        ]
    },
    {
        "nombre": "No invertir",
        "resultados": [
            ({"ganancia": 3000, "costo": 500}, 1.0)     # resultado seguro
        ]
    }
]


# ====================== EJECUCIÓN =====================================

mejor = mejor_decision(acciones)

print("\n[Red de Decisión]")
print("Mejor decisión:", mejor["nombre"])

