#¿Qué es la Comprobación hacia Adelante (Forward Checking)?
#Es una técnica de búsqueda inteligente para problemas CSP que mejora el Backtracking tradicional. 
# Mientras que el Backtracking solo mira hacia atrás para ver si la asignación actual es válida, 
# el Forward Checking mira hacia el futuro.

#Cómo funciona:

#Filtrado de Dominios: Cada vez que se asigna un valor a una variable, el algoritmo revisa a sus 
# vecinos no asignados y elimina de sus "opciones disponibles" (dominios) cualquier valor que cause 
# conflicto.

#Detección Temprana de Fallos: Si al eliminar una opción, el dominio de una variable vecina se queda 
# vacío (len == 0), el algoritmo sabe inmediatamente que la decisión actual es un error y retrocede 
# sin perder tiempo explorando esa rama.

#Eficiencia: Reduce drásticamente el espacio de búsqueda al podar ramas que "están condenadas al 
# fracaso" antes de siquiera visitarlas.

# Turnos de la central de emergencias
turnos = ['Mañana', 'Tarde', 'Noche']

# Tipos de guardia (Personal disponible)
personal_disponible = ['Equipo-Alfa', 'Equipo-Beta']

# Restricciones: Turnos que no pueden solaparse con el mismo personal
conflictos_horarios = {
    'Mañana': ['Tarde'],
    'Tarde': ['Mañana', 'Noche'],
    'Noche': ['Tarde']
}

def gestion_preventiva(asignacion_actual=None, opciones_restantes=None):
    """
    Asigna personal a turnos usando Forward Checking para predecir colapsos de horario.
    """
    if asignacion_actual is None:
        asignacion_actual = {}

    # Inicializamos los dominios de cada turno con todo el personal disponible
    if opciones_restantes is None:
        opciones_restantes = {t: list(personal_disponible) for t in turnos}

    # Caso base: Todos los turnos han sido cubiertos con éxito
    if len(asignacion_actual) == len(turnos):
        print("\n[PLANIFICACIÓN EXITOSA]:", asignacion_actual)
        return asignacion_actual

    # Seleccionamos el siguiente turno a cubrir
    turno_actual = turnos[len(asignacion_actual)]

    # Intentamos asignar a un equipo del dominio actual de ese turno
    for equipo in opciones_restantes[turno_actual]:
        print(f"Evaluando '{equipo}' para el turno de la {turno_actual}...")

        # Creamos una copia de las opciones futuras para simular el impacto
        futuro_proyectado = {t: list(opciones_restantes[t]) for t in opciones_restantes}
        asignacion_actual[turno_actual] = equipo

        alerta_de_vacio = False

        # --- MECANISMO DE VIGILANCIA (Forward Checking) ---
        for turno_vecino in conflictos_horarios[turno_actual]:
            # Si el equipo elegido está en las opciones del turno vecino, lo eliminamos
            if equipo in futuro_proyectado[turno_vecino]:
                futuro_proyectado[turno_vecino].remove(equipo)
                print(f"  -> Reduciendo opciones para {turno_vecino}. Quedan: {futuro_proyectado[turno_vecino]}")

                # VALIDACIÓN CRÍTICA: Si el futuro vecino se queda sin personal, es un fallo
                if not futuro_proyectado[turno_vecino]:
                    print(f"  [!] ALERTA: {turno_vecino} se quedaría sin personal. Abortando elección.")
                    alerta_de_vacio = True

        # Si el movimiento no bloquea el futuro, seguimos adelante (Recursión)
        if not alerta_de_vacio:
            resultado = gestion_preventiva(asignacion_actual, futuro_proyectado)
            if resultado:
                return resultado

        # Si falló o la recursión no prosperó, liberamos el turno (Backtrack)
        del asignacion_actual[turno_actual]

    return None

# --- INICIO DEL SISTEMA DE GUARDIAS ---
print("--- Iniciando Protocolo de Asignación con Forward Checking ---")
gestion_preventiva()