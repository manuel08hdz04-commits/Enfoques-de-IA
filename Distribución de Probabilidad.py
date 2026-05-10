#¿Qué es una Distribución de Probabilidad?
#Una Distribución de Probabilidad es un mapa que nos indica qué tan posible es cada uno de los 
# resultados de un experimento aleatorio. En IA, es el "perfil" o "huella digital" de un fenómeno.

#Componentes clave:

#Frecuencia Relativa: La base del aprendizaje. Si un evento ocurre 5 veces de cada 10, su 
# probabilidad es 0.5.

#Espacio Muestral: El conjunto de todos los resultados posibles (en este caso: manzana, plátano, 
# naranja).

#Selección por Ruleta: Es una forma de transformar probabilidades en decisiones. Imagina una ruleta 
# donde el tamaño de cada sección es proporcional a su probabilidad; al girarla, los eventos más 
# probables tienen más opciones de ganar, pero los menos probables aún conservan una pequeña 
# oportunidad (evitando que la IA sea 100% predecible).

import random

# --- MOTOR DE ANÁLISIS DE PREFERENCIAS ---

def modelar_preferencias(historial):
    """
    Transforma datos crudos en una Función de Probabilidad de Masa (PMF).
    """
    total = len(historial)
    conteo = {}
    
    # 1. Fase de conteo (Frecuencia Absoluta)
    for item in historial:
        conteo[item] = conteo.get(item, 0) + 1
        
    # 2. Fase de normalización (Distribución de Probabilidad)
    distribucion = {item: cant / total for item, cant in conteo.items()}
    return distribucion

def motor_prediccion_ruleta(distribucion):
    """
    Simula una decisión basada en la distribución aprendida.
    """
    disparo = random.random() # Número entre 0.0 y 1.0
    acumulado = 0.0
    
    for item, prob in distribucion.items():
        acumulado += prob
        if disparo <= acumulado:
            return item
    return list(distribucion.keys())[-1]

# --- ESCENARIO: Historial de pedidos de un cliente ---
datos_cliente = [
    'Café', 'Café', 'Café', 'Café', 'Café', 'Café', # 60%
    'Té', 'Té',                                     # 20%
    'Jugo', 'Jugo'                                  # 20%
]

# 1. Entrenamiento del perfil
perfil_usuario = modelar_preferencias(datos_cliente)

print("--- PERFIL DE PROBABILIDAD APRENDIDO ---")
for producto, p in perfil_usuario.items():
    barra = "█" * int(p * 20)
    print(f" {producto.ljust(6)}: {p*100:>3.0f}% | {barra}")

# 2. Generación de sugerencias
print("\n--- SUGERENCIAS GENERADAS POR IA (10 DÍAS) ---")
sugerencias = [motor_prediccion_ruleta(perfil_usuario) for _ in range(10)]

# Resumen de resultados
for i, s in enumerate(sugerencias, 1):
    print(f" Día {i:02d}: Sugerir {s}")

print(f"\nResumen de la IA: {sugerencias}")
