#¿Qué es el Manto de Markov?
#En una Red Bayesiana, el Manto de Markov de un nodo es su "vecindad inmediata" de influencia. Es el 
# conjunto mínimo de nodos que, si se conocen con certeza, hacen que el nodo objetivo sea totalmente 
# independiente de todos los demás nodos de la red.

#Imagina que quieres predecir si un paciente tiene una enfermedad. Si tienes toda la información de su 
# Manto de Markov, saber cualquier otra cosa sobre el hospital, el clima o el historial de otros 
# pacientes es irrelevante; ya tienes el "escudo" informativo completo.

#El Manto de Markov se compone de:

#Sus Padres: Las causas directas.

#Sus Hijos: Los efectos directos.

#Los Co-padres de sus hijos: Otras variables que causan los mismos efectos (necesarias para evitar el 
# efecto de "explicación alternativa").

# --- MOTOR DE EXTRACCIÓN DE MANTO DE MARKOV ---

def extraer_escudo_informativo(red, nodo):
    """
    Identifica el Manto de Markov para aislar un nodo del resto del sistema.
    """
    if nodo not in red:
        return "Nodo no encontrado."

    padres = set(red[nodo]['padres'])
    hijos = set()
    copadres = set()

    # Buscamos hijos y sus respectivos co-padres
    for potencial_hijo, config in red.items():
        if nodo in config['padres']:
            hijos.add(potencial_hijo)
            # Si encontramos un hijo, agregamos a sus otros padres (co-padres)
            for p in config['padres']:
                if p != nodo:
                    copadres.add(p)

    # El Manto es la unión de estos tres grupos
    manto = padres.union(hijos).union(copadres)
    
    return {
        "Padres": list(padres),
        "Hijos": list(hijos),
        "Co-padres": list(copadres),
        "Manto_Total": list(manto)
    }

# --- ESCENARIO: Red de Diagnóstico de Infraestructura ---
# Queremos saber qué afecta y qué es afectado por una 'Falla_de_Servidor'
red_it = {
    'Corte_Energia':   {'padres': []},
    'Error_Hardware':  {'padres': []},
    'Falla_Servidor':  {'padres': ['Corte_Energia', 'Error_Hardware']}, # Objetivo
    'Alerta_Email':    {'padres': ['Falla_Servidor']},
    'Web_Caida':       {'padres': ['Falla_Servidor', 'Mantenimiento_DNS']},
    'Mantenimiento_DNS': {'padres': []},
    'Queja_Cliente':   {'padres': ['Web_Caida']}
}

objetivo = 'Falla_Servidor'
manto = extraer_escudo_informativo(red_it, objetivo)

print(f"--- ANALIZANDO AISLAMIENTO PARA: {objetivo} ---")
print(f"1. Causas (Padres):    {manto['Padres']}")
print(f"2. Efectos (Hijos):    {manto['Hijos']}")
print(f"3. Co-causas (Co-pad): {manto['Co-padres']}")

print("\n" + "="*50)
print(f" ESCUDO DE MARKOV: {manto['Manto_Total']} ")
print("="*50)
print(f"Nota IA: Si conocemos el estado de estos {len(manto['Manto_Total'])} nodos,")
print(f"la variable '{objetivo}' queda blindada contra cambios en el resto de la red.")