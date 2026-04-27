'''
RED BAYESIANA DINÁMICA

Modelo probabilístico en el tiempo.

Ejemplo: evolución del clima día a día.
'''

# ====================== TRANSICIÓN =====================================

def siguiente_estado(actual):
    if actual == "Soleado":
        return {"Soleado": 0.7, "Lluvia": 0.3}
    else:
        return {"Soleado": 0.4, "Lluvia": 0.6}


# ====================== SIMULACIÓN =====================================

def simular_clima(inicial, pasos):
    estado = inicial

    for t in range(pasos):
        probs = siguiente_estado(estado)

        # Elegir el más probable (simplificación)
        estado = max(probs, key=probs.get)

        print(f"Día {t+1}: {estado}")


# ====================== EJEMPLO ========================================

print("\n[Clima dinámico:]")
simular_clima("Soleado", 5)
