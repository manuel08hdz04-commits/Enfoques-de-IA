# ----------------------------------------
# RED DE DECISIÓN - ELECCIÓN DE INVERSIÓN
# ----------------------------------------

# Función de utilidad: calcula beneficio neto
def utilidad(estado):
    # ganancia menos costo
    return estado["ganancia"] - estado["costo"]


# Función que elige la mejor decisión
def mejor_decision(acciones):
    mejor_accion = None
    mejor_valor = float("-inf")  # valor inicial muy bajo

    # Evaluar cada acción disponible
    for accion in acciones:
        valor_total = 0  # valor esperado de la acción

        # Recorrer los posibles resultados de esa acción
        for resultado, probabilidad in accion["resultados"]:
            valor_total += probabilidad * utilidad(resultado)

        # Comparar con la mejor opción encontrada
        if valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_accion = accion

    return mejor_accion


# ----------------------------------------
# EJEMPLO REAL: DECIDIR SI INVERTIR
# ----------------------------------------

acciones = [
    {
        "nombre": "Invertir",
        "resultados": [
            ({"ganancia": 10000, "costo": 2000}, 0.6),  # caso exitoso
            ({"ganancia": 2000, "costo": 2000}, 0.4)    # caso no exitoso
        ]
    },
    {
        "nombre": "No invertir",
        "resultados": [
            ({"ganancia": 3000, "costo": 500}, 1.0)     # resultado seguro
        ]
    }
]

# Ejecutar el algoritmo
mejor = mejor_decision(acciones)

# Mostrar resultado
print("Mejor decisión:", mejor["nombre"])
