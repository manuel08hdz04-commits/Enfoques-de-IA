#¿Qué es la Eliminación de Variables?
#Es un algoritmo de programación dinámica que optimiza el cálculo de probabilidades en Redes 
# Bayesianas. En lugar de recalcular las mismas multiplicaciones una y otra vez (como hace la 
# recursión simple), este método transforma las Tablas de Probabilidad Condicional (CPT) en Factores.

#El proceso de "Destilación":

#Multiplicación de Factores: Combina piezas de información relacionadas.

#Marginalización (Sumar y Eliminar): Elimina una variable oculta sumando sus posibilidades, 
# "colapsando" esa dimensión del problema.

#Orden de Eliminación: El orden en que borramos las variables afecta drásticamente la velocidad, 
# permitiendo resolver redes que la enumeración simple no podría manejar.

import itertools

# --- CLASE FACTOR: La unidad de información ---
class Factor:
    def __init__(self, variables, tabla):
        self.variables = variables # Lista de variables involucradas
        self.tabla = tabla         # Diccionario: { (Valores): Probabilidad }

# --- FUNCIONES DE MANIPULACIÓN DE FACTORES ---

def multiplicar(f1, f2):
    """Combina dos factores multiplicando sus probabilidades en mundos compatibles."""
    nuevas_vars = list(set(f1.variables + f2.variables))
    tabla_nueva = {}
    
    for comb in itertools.product([True, False], repeat=len(nuevas_vars)):
        estado = dict(zip(nuevas_vars, comb))
        t1, t2 = tuple(estado[v] for v in f1.variables), tuple(estado[v] for v in f2.variables)
        
        if t1 in f1.tabla and t2 in f2.tabla:
            tabla_nueva[comb] = f1.tabla[t1] * f2.tabla[t2]
            
    return Factor(nuevas_vars, tabla_nueva)

def marginalizar(factor, var_eliminar):
    """Elimina una variable sumando sus probabilidades (colapso de datos)."""
    nuevas_vars = [v for v in factor.variables if v != var_eliminar]
    tabla_nueva = {}
    
    for comb, prob in factor.tabla.items():
        estado = dict(zip(factor.variables, comb))
        tupla_reducida = tuple(estado[v] for v in nuevas_vars)
        tabla_nueva[tupla_reducida] = tabla_nueva.get(tupla_reducida, 0) + prob
        
    return Factor(nuevas_vars, tabla_nueva)

# --- ALGORITMO PRINCIPAL ---

def motor_eliminacion_variables(consulta, evidencia, red):
    # 1. Crear factores iniciales aplicando la evidencia (poda de ramas)
    factores = []
    for nodo, config in red.items():
        vars_f = config['padres'] + [nodo]
        tabla_f = {}
        for comb in itertools.product([True, False], repeat=len(vars_f)):
            est = dict(zip(vars_f, comb))
            if all(est[v] == val for v, val in evidencia.items() if v in est):
                p_true = config['cpt'][tuple(est[p] for p in config['padres'])]
                tabla_f[comb] = p_true if est[nodo] else (1.0 - p_true)
        factores.append(Factor(vars_f, tabla_f))

    # 2. Identificar y eliminar variables irrelevantes
    ocultas = [n for n in red if n != consulta and n not in evidencia]
    
    for v in ocultas:
        # Extraer factores que mencionan a 'v'
        relacionados = [f for f in factores if v in f.variables]
        factores = [f for f in factores if v not in f.variables]
        
        if relacionados:
            f_unido = relacionados[0]
            for f in relacionados[1:]: f_unido = multiplicar(f_unido, f)
            factores.append(marginalizar(f_unido, v))

    # 3. Combinar resultados finales
    res = factores[0]
    for f in factores[1:]: res = multiplicar(res, f)
    
    # Normalización final (Alfa)
    total = sum(res.tabla.values())
    return {c[0]: p / total for c, p in res.tabla.items()}

# --- DATOS DE PRUEBA (Mismo escenario Alarma) ---
red_alarma = {
    'Robo': {'padres': [], 'cpt': {(): 0.001}},
    'Terremoto': {'padres': [], 'cpt': {(): 0.002}},
    'Alarma': {'padres': ['Robo', 'Terremoto'], 'cpt': {(True, True): 0.95, (True, False): 0.94, (False, True): 0.29, (False, False): 0.001}},
    'JuanLlama': {'padres': ['Alarma'], 'cpt': {(True,): 0.90, (False,): 0.05}},
    'MariaLlama': {'padres': ['Alarma'], 'cpt': {(True,): 0.70, (False,): 0.01}}
}

final = motor_eliminacion_variables('Robo', {'JuanLlama': True, 'MariaLlama': True}, red_alarma)
print(f"Probabilidad de Robo tras eliminar variables: {final[True]*100:.2f}%")
