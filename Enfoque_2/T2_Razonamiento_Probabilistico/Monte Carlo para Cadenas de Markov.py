#¿Qué es MCMC y Metropolis-Hastings?
# Cuando una distribución es tan compleja que no podemos usar muestreo por rechazo (porque 
# desperdiciaríamos años) ni ponderación de verosimilitud (porque la red es demasiado grande), 
# usamos MCMC.

# La idea central: En lugar de generar muestras independientes desde cero, creamos una Cadena de 
# Markov: un proceso donde cada nueva muestra depende de la anterior. Es como una caminata 
# aleatoria que, con el tiempo, prefiere quedarse en las zonas de alta probabilidad.

# El algoritmo Metropolis-Hastings funciona así:
# Propuesta: Desde donde estás ($x_{actual}$), das un paso al azar hacia un nuevo punto 
# ($x_{propuesto}$).
# Evaluación: * ¿El nuevo punto es más "alto" (más probable)? Vas hacia allá.¿El nuevo punto es 
# más "bajo"? Lanzas un dado. Tienes una oportunidad de ir, pero también de quedarte donde estás.
# Equilibrio: Eventualmente, el explorador pasará más tiempo en las cimas que en los valles, 
# dibujando perfectamente la forma de la montaña.

import random
import math

# --- 1. EL TERRENO: La montaña que queremos mapear ---
def mapa_probabilidad(x):
    """
    Representa la 'altura' del terreno en el punto x.
    Usamos una distribución Normal (Campana de Gauss).
    """
    # Altura relativa de la campana en x
    return math.exp(-0.5 * (x**2))

# --- 2. EL EXPLORADOR: Algoritmo Metropolis-Hastings ---
def explorador_mcmc(pasos, tamaño_salto=0.5):
    """
    Realiza una caminata aleatoria para muestrear la distribución.
    """
    muestras = []
    x_actual = 0.0  # Punto de partida del explorador
    exitos = 0
    
    print(f"[*] Iniciando expedición de {pasos} pasos...")

    for _ in range(pasos):
        # A. Proponer un movimiento (Caminar hacia un lado)
        x_propuesto = random.gauss(x_actual, tamaño_salto)
        
        # B. Comparar alturas (Probabilidades)
        altura_actual = mapa_probabilidad(x_actual)
        altura_propuesta = mapa_probabilidad(x_propuesto)
        
        # C. Criterio de Aceptación (La regla de oro)
        ratio_aceptacion = altura_propuesta / altura_actual
        
        # Si el ratio es > 1, aceptamos siempre. Si es < 1, aceptamos con prob p.
        if random.random() < ratio_aceptacion:
            x_actual = x_propuesto
            exitos += 1
            
        # IMPORTANTE: En MCMC, incluso si rechazamos, 
        # la posición actual cuenta como una muestra válida.
        muestras.append(x_actual)
        
    tasa = (exitos / pasos) * 100
    return muestras, tasa

# --- 3. ANÁLISIS DE LA EXPEDICIÓN ---
n_pasos = 10000
camino, eficiencia = explorador_mcmc(n_pasos)

print("\n" + "="*40)
print("   REPORTE DE EXPLORACIÓN MCMC")
print("="*40)
print(f"Pasos totales:      {n_pasos}")
print(f"Tasa de movimiento: {eficiencia:.2f}%")
print(f"Media encontrada:   {sum(camino)/len(camino):.4f} (Objetivo: 0.0)")

# Visualización rápida del "camino" tomado por el explorador
print("\n[Rastro de los primeros pasos]:")
print(" -> ".join([f"{s:.2f}" for s in camino[:8]]) + " ...")
