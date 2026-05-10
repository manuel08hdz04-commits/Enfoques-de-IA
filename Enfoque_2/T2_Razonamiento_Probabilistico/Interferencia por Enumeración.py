#¿Qué es la Inferencia por Enumeración?
#Es el método de "fuerza bruta inteligente" para responder preguntas en una Red Bayesiana. Cuando 
# queremos saber la probabilidad de un evento (consulta) dada cierta evidencia, el algoritmo debe 
# lidiar con las variables ocultas (aquellas de las que no sabemos nada).

#El proceso se divide en dos grandes acciones:

#Marginalización (Suma): Para las variables que no conocemos, la IA explora "mundos paralelos": ¿qué 
# pasaría si la variable fuera verdadera? ¿y si fuera falsa? Luego, suma ambas posibilidades para 
# eliminarlas de la ecuación.

#Regla de la Cadena (Producto): Multiplica las probabilidades condicionales a lo largo de las ramas 
# de la red para calcular la probabilidad conjunta de cada escenario.

# --- MOTOR DE INFERENCIA POR ENUMERACIÓN ---

def obtener_p(nodo, valor, evidencia, red):
    """Extrae P(Variable | Padres) de la CPT."""
    config_padres = tuple(evidencia[p] for p in red[nodo]['padres'])
    prob_true = red[nodo]['cpt'][config_padres]
    return prob_true if valor else (1.0 - prob_true)

def enumerar_recursivo(variables, evidencia, red):
    """
    Explora recursivamente el árbol de probabilidades.
    Implementa la sumatoria sobre variables ocultas (Marginalización).
    """
    if not variables:
        return 1.0 # Caso base: fin de la cadena
    
    Y = variables[0]
    resto = variables[1:]
    
    if Y in evidencia:
        # Si conocemos Y, simplemente multiplicamos su probabilidad y seguimos
        return obtener_p(Y, evidencia[Y], evidencia, red) * enumerar_recursivo(resto, evidencia, red)
    else:
        # Si Y es oculta, sumamos los casos True y False (Marginalización)
        suma = 0
        for valor in [True, False]:
            evidencia_ext = evidencia.copy()
            evidencia_ext[Y] = valor
            suma += obtener_p(Y, valor, evidencia_ext, red) * enumerar_recursivo(resto, evidencia_ext, red)
        return suma

def motor_inferencia(consulta, evidencia, red):
    """Calcula la distribución normalizada P(Consulta | Evidencia)."""
    resultados = {}
    vars_ordenadas = list(red.keys())
    
    for valor_c in [True, False]:
        evidencia_copy = evidencia.copy()
        evidencia_copy[consulta] = valor_c
        resultados[valor_c] = enumerar_recursivo(vars_ordenadas, evidencia_copy, red)
    
    # Normalización (Constante Alfa)
    total = sum(resultados.values())
    return {v: p / total for v, p in resultados.items()}

# --- CONFIGURACIÓN DE LA RED (Red de Alarma de Pearl) ---
red_seguridad = {
    'Robo':      {'padres': [], 'cpt': {(): 0.001}},
    'Terremoto': {'padres': [], 'cpt': {(): 0.002}},
    'Alarma':    {'padres': ['Robo', 'Terremoto'], 'cpt': {
        (True, True): 0.95, (True, False): 0.94, (False, True): 0.29, (False, False): 0.001}},
    'JuanLlama': {'padres': ['Alarma'], 'cpt': {(True,): 0.90, (False,): 0.05}},
    'MariaLlama':{'padres': ['Alarma'], 'cpt': {(True,): 0.70, (False,): 0.01}}
}

# --- EJECUCIÓN DEL MISTERIO ---
# Evidencia: Juan y María llaman.
evidencia = {'JuanLlama': True, 'MariaLlama': True}
prob_robo = motor_inferencia('Robo', evidencia, red_seguridad)

print(f"--- DIAGNÓSTICO DEL SISTEMA ---")
print(f"Evidencia: Reportes de Juan y María recibidos.")
print(f"Probabilidad de Robo Real: {prob_robo[True]*100:.2f}%")
print(f"Probabilidad de Confusión/Error: {prob_robo[False]*100:.2f}%")
