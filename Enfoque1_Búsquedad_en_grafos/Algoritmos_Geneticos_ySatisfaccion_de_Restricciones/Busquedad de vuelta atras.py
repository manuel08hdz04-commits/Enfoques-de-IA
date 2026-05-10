#¿Qué es el Backtracking?
#El Backtracking es una estrategia de búsqueda exhaustiva que construye soluciones candidatas paso a 
# paso. Su característica principal es que, en cuanto se da cuenta de que una solución parcial no 
# puede completarse de forma válida, retrocede (hace "backtrack") al paso anterior para probar una 
# alternativa diferente.

#Cómo funciona:

#Recursión: Intenta asignar un valor a la variable actual y llama a la función para la siguiente.

#Poda: Si ninguna opción funciona para la variable actual, el algoritmo admite que el error ocurrió 
# antes, borra su decisión actual y regresa al nivel anterior.

#Eficiencia: Es mucho más inteligente que la fuerza bruta pura, ya que descarta ramas enteras de 
# posibilidades en cuanto detecta que violan una regla.

# Invitados a la mesa principal
invitados = ['Duque A', 'Conde B', 'Barón C']

# Opciones de menú disponibles para evitar disputas
opciones_menu = ['Pescado', 'Carne']

# Mapa de rivalidades (Invitados que no pueden repetir menú si están cerca)
rivalidades = {
    'Duque A': ['Conde B'],
    'Conde B': ['Duque A', 'Barón C'],
    'Barón C': ['Conde B']
}

def protocolo_seguro(persona, plato, mesa_actual):
    """
    Verifica si servir un plato a un invitado causará un conflicto con sus rivales.
    """
    enemigos = rivalidades.get(persona, [])
    for rival in enemigos:
        # Si el rival ya está sentado y tiene el mismo plato...
        if rival in mesa_actual and mesa_actual[rival] == plato:
            return False  # Conflicto detectado
    return True

# --- MOTOR DE BACKTRACKING ---

def organizar_banquete(mesa=None):
    """
    Asigna platos de forma recursiva, retrocediendo si llega a un callejón sin salida.
    """
    if mesa is None:
        mesa = {}

    # Condición de éxito: Todos los invitados tienen un plato asignado
    if len(mesa) == len(invitados):
        print("\n[Protocolo Finalizado] Configuración de mesa exitosa:", mesa)
        return mesa

    # Seleccionamos al siguiente invitado en la lista
    sujeto_actual = invitados[len(mesa)]

    for plato in opciones_menu:
        print(f"Probando {plato} para {sujeto_actual}...")

        if protocolo_seguro(sujeto_actual, plato, mesa):
            # Realizamos la asignación temporal
            mesa[sujeto_actual] = plato
            
            # Intentamos resolver el resto del banquete con esta decisión
            resultado = organizar_banquete(mesa)
            
            if resultado:
                return resultado
            
            # Si el código llega aquí, es porque la decisión anterior causó un fallo después
            print(f"  [!] Rebobinando: {sujeto_actual} no puede comer {plato}. Regresando...")
            del mesa[sujeto_actual] # Este es el paso de "Backtrack"

    return None # No hay solución posible en esta rama

# --- INICIO DEL PROTOCOLO REAL ---
organizar_banquete()