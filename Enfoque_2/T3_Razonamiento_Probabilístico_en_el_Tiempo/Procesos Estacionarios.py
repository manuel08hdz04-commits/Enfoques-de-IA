#¿Qué es un Proceso Estacionario?
#En términos simples, un proceso es estacionario si sus propiedades estadísticas (como la media, 
# la varianza y la autocorrelación) no cambian a lo largo del tiempo.

#Imaginalo así:

#Proceso Estacionario: Es como el ruido de fondo de un café. Puede subir o bajar un poco, pero el 
# nivel promedio de ruido es constante.

#Proceso NO Estacionario: Es como el precio de una acción o la temperatura global. Tienen tendencias, 
# ciclos o cambios de volatilidad que hacen que el "promedio" de hoy no sirva para predecir el de 
# dentro de diez años.

import random
import math

# --- 1. GENERADORES DE SEÑALES ---

def generar_proceso_estacionario(n=100):
    """Genera ruido blanco: media constante, varianza constante."""
    return [random.gauss(0, 1) for _ in range(n)]

def generar_proceso_no_estacionario(n=100):
    """Genera una caminata aleatoria con tendencia (Trend)."""
    serie = []
    valor_actual = 0
    for i in range(n):
        paso = random.gauss(0.2, 1) # El 0.2 crea una tendencia alcista
        valor_actual += paso
        serie.append(valor_actual)
    return serie

# --- 2. ANALIZADOR ESTADÍSTICO ---

def analizar_estacionariedad(serie, nombre):
    """Divide la serie en dos mitades y compara sus estadísticas."""
    mitad = len(serie) // 2
    parte1 = serie[:mitad]
    parte2 = serie[mitad:]
    
    media1 = sum(parte1) / len(parte1)
    media2 = sum(parte2) / len(parte2)
    
    varianza1 = sum((x - media1)**2 for x in parte1) / len(parte1)
    varianza2 = sum((x - media2)**2 for x in parte2) / len(parte2)
    
    print(f"\n--- Análisis: {nombre} ---")
    print(f"Media Mitad A: {media1:.2f} | Media Mitad B: {media2:.2f}")
    print(f"Var.  Mitad A: {varianza1:.2f} | Var.  Mitad B: {varianza2:.2f}")
    
    # Un proceso es estacionario si las métricas son muy similares
    dif_media = abs(media1 - media2)
    if dif_media < 0.5: # Umbral simplificado
        print("Resultado: Probablemente ESTACIONARIO (Estable)")
    else:
        print("Resultado: NO ESTACIONARIO (Tiene tendencia o cambios)")

# --- 3. EJECUCIÓN ---

# Generamos datos
datos_estables = generar_proceso_estacionario(200)
datos_tendencia = generar_proceso_no_estacionario(200)

# Analizamos
analizar_estacionariedad(datos_estables, "Ruido Blanco (Estacionario)")
analizar_estacionariedad(datos_tendencia, "Caminata Aleatoria (No Estacionario)")