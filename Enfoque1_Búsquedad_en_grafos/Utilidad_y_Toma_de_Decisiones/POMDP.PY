'''
POMDP - PROCESO DE DECISIÓN PARCIALMENTE OBSERVABLE

El agente NO sabe exactamente en qué estado está,
usa creencias (probabilidades).

Ejemplo: decidir salir sin saber si hay tráfico real.
'''

# ====================== ACTUALIZACIÓN DE CREENCIA ======================

def actualizar_creencia(creencia, accion, observacion, modelo):
    nueva_creencia = {}

    for s in modelo["estados"]:
        prob = 0

        # 🔹 Suma sobre estados anteriores
        for s_prev in modelo["estados"]:
            prob += (
                creencia[s_prev] *
                modelo["transiciones"][s_prev][accion][s]
            )

        # 🔹 Multiplicar por probabilidad de observación
        prob *= modelo["observaciones"][s][observacion]

        nueva_creencia[s] = prob

    # 🔹 Normalizar
    total = sum(nueva_creencia.values())
    for s in nueva_creencia:
        nueva_creencia[s] /= total

    return nueva_creencia


# ====================== EJEMPLO ========================================

modelo = {
    "estados": ["Libre", "Tráfico"],
    "transiciones": {
        "Libre": {"salir": {"Libre": 0.7, "Tráfico": 0.3}},
        "Tráfico": {"salir": {"Libre": 0.4, "Tráfico": 0.6}}
    },
    "observaciones": {
        "Libre": {"rapido": 0.8, "lento": 0.2},
        "Tráfico": {"rapido": 0.3, "lento": 0.7}
    }
}

creencia = {"Libre": 0.6, "Tráfico": 0.4}

print("\n[POMDP:]")
print(actualizar_creencia(creencia, "salir", "lento", modelo))
