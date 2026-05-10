#¿Qué son la Condición y la Normalización?
# Estos dos procesos permiten a la IA pasar de "datos brutos" a "decisiones lógicas":Probabilidad 
# Condicionada $P(B|A)$: Es la probabilidad de que ocurra un evento $B$ dado que ya ocurrió el evento
#  $A$. 

# En nuestro caso: "¿Cuál es la probabilidad de que llueva mañana dado que hoy está nublado?". 
# La IA no mira el pasado lejano, solo el estado actual.Normalización: Es el proceso matemático 
# de ajustar los valores para que su suma sea exactamente 1.0 (100%). 
# Esto es vital porque en el mundo real, algo tiene que pasar; no podemos tener un escenario donde 
# las probabilidades sumen 80% o 120%.

import random

# --- MOTOR DE TRANSICIÓN ATMOSFÉRICA ---

# 1. DATOS HISTÓRICOS (Conteos crudos de observaciones pasadas)
# Estos números representan cuántas veces ocurrió una transición X -> Y
registros_crudos = {
    'Soleado':  {'Soleado': 120, 'Nublado': 30,  'Lluvioso': 10},
    'Nublado':  {'Soleado': 50,  'Nublado': 100, 'Lluvioso': 50},
    'Lluvioso': {'Soleado': 10,  'Nublado': 40,  'Lluvioso': 80}
}

def generar_matriz_probabilidades(datos):
    """
    Transforma conteos en probabilidades condicionadas normalizadas.
    """
    matriz = {}
    for estado_hoy, transiciones in datos.items():
        # NORMALIZACIÓN: Suma total de salidas desde el estado 'hoy'
        total_observaciones = sum(transiciones.values())
        
        # P(Mañana | Hoy) = Conteo / Total
        matriz[estado_hoy] = {
            futuro: (conteo / total_observaciones) 
            for futuro, conteo in transiciones.items()
        }
    return matriz

# 2. FASE DE APRENDIZAJE: Normalización de la Matriz
print("[SISTEMA]: Procesando registros históricos y normalizando...")
matriz_markov = generar_matriz_probabilidades(registros_crudos)

# 3. MOTOR DE INFERENCIA CONDICIONADA
def simular_clima(estado_actual, pasos=5):
    print(f"\n--- PRONÓSTICO INICIANDO EN: {estado_actual.upper()} ---")
    
    hoy = estado_actual
    for i in range(1, pasos + 1):
        # Extraemos la fila de la matriz condicionada al estado actual
        distribucion_prob = matriz_markov[hoy]
        
        opciones = list(distribucion_prob.keys())
        probabilidades = list(distribucion_prob.values())
        
        # El 'dado' de la IA se lanza usando los pesos normalizados
        manana = random.choices(opciones, weights=probabilidades, k=1)[0]
        
        print(f" Día {i}: {manana.ljust(10)} (P={distribucion_prob[manana]*100:>4.1f}%)")
        hoy = manana # El futuro se vuelve el presente

# --- EJECUCIÓN ---
simular_clima('Lluvioso', 7)
