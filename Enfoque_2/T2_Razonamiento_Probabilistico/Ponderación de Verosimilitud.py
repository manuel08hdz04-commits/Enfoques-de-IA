#¿Qué es la Ponderación de Verosimilitud?
#Es un algoritmo de muestreo aproximado para Redes Bayesianas. El problema del muestreo tradicional 
# es que, si buscas un evento muy raro, pasarías años rechazando muestras.

#La Ponderación de Verosimilitud soluciona esto con dos reglas:

#Consistencia: Si sabemos que un evento ocurrió (Evidencia), forzamos a que ocurra en todas las 
# simulaciones. Nunca lo dejamos al azar.

#Ponderación: Como estamos haciendo "trampa" al forzar eventos, cada simulación recibe un peso. Si 
# forzamos un evento que era muy improbable, la simulación pierde peso. Si forzamos algo que era muy 
# lógico, mantiene su peso alto.

import random

# --- 1. EL MODELO: ¿Por qué está mojado el suelo? ---
# P(Nubes) -> P(Lluvia|Nubes) -> P(SueloMojado|Lluvia, Regador)

def simular_detective(evidencia):
    """
    Genera un universo donde los hechos conocidos se fuerzan, 
    ajustando el peso de la realidad.
    """
    peso = 1.0
    mundo = {}

    # Variable 1: CIELO (Azar)
    mundo['Cielo'] = 'Nublado' if random.random() < 0.5 else 'Despejado'

    # Variable 2: LLUVIA (Evidencia: Sabemos que NO llovió)
    # En lugar de tirar dados, forzamos el hecho y ajustamos el peso.
    cielo = mundo['Cielo']
    if 'Lluvia' in evidencia:
        mundo['Lluvia'] = evidencia['Lluvia']
        # Peso *= P(Lluvia=No | Cielo)
        prob_no_lluvia = 0.2 if cielo == 'Nublado' else 0.9
        peso *= prob_no_lluvia

    # Variable 3: REGADOR (Azar)
    # No es evidencia, así que dejamos que la simulación decida.
    prob_encendido = 0.1 if cielo == 'Nublado' else 0.5
    mundo['Regador'] = 'Encendido' if random.random() < prob_encendido else 'Apagado'

    # Variable 4: SUELO MOJADO (Evidencia: Sabemos que ESTÁ mojado)
    if 'Suelo' in evidencia:
        mundo['Suelo'] = evidencia['Suelo']
        # Calculamos la verosimilitud de este suelo mojado dado el resto del mundo
        if mundo['Regador'] == 'Encendido' and mundo['Lluvia'] == 'No':
            verosimilitud = 0.9  # Muy probable si el regador estuvo prendido
        else:
            verosimilitud = 0.01 # Casi imposible si nada lo mojó
        peso *= verosimilitud

    return mundo['Regador'], peso

# --- 2. EJECUCIÓN DEL MUESTREO ---
# Hechos: El suelo está mojado, pero el cielo estuvo despejado (no llovió).
hechos = {'Suelo': 'Si', 'Lluvia': 'No'}
acumulador_pesos = {'Encendido': 0.0, 'Apagado': 0.0}

for _ in range(10000):
    estado_regador, peso_final = simular_detective(hechos)
    acumulador_pesos[estado_regador] += peso_final

# --- 3. ANALÍTICA FINAL ---
total_p = sum(acumulador_pesos.values())
prob_final = (acumulador_pesos['Encendido'] / total_p) * 100

print(f"--- ANÁLISIS DE VEROSIMILITUD ---")
print(f"Evidencia: Suelo Mojado + Sin Lluvia")
print(f"Probabilidad de que el Regador causara esto: {prob_final:.2f}%")