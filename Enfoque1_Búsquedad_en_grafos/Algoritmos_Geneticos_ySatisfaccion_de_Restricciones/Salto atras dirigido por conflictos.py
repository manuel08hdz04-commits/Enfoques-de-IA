#¿Qué es el Salto Atrás (Backjumping)?
#El Backjumping es una técnica de optimización para algoritmos de Backtracking. Mientras que el 
# Backtracking tradicional retrocede un solo paso cuando falla (hacia el padre inmediato), el 
# Backjumping analiza qué variables causaron realmente el conflicto y tiene la capacidad de saltar 
# varios niveles hacia atrás en el árbol de búsqueda.

#Cómo funciona:

#Análisis de Conflictos: El algoritmo mantiene un registro de qué variables previas impidieron que 
# la variable actual tomara un valor válido.

#Salto Inteligente: Si la variable actual no tiene opciones, no sirve de nada retroceder a la variable 
# anterior si esta no tiene nada que ver con el conflicto. El algoritmo "salta" directamente a la 
# variable que originó la restricción.

#Eficiencia: Ahorra una cantidad masiva de tiempo al ignorar ramas del árbol de búsqueda que no tienen 
# posibilidad de solucionar el conflicto actual.

# Satélites en órbita que requieren configuración
satelites = ['Sat-A', 'Sat-B', 'Sat-C']

# Canales de frecuencia de transmisión
canales = ['Frecuencia-1', 'Frecuencia-2']


# Mapa de Interferencia (Satélites cercanos que no pueden compartir canal)
interferencias_orbitantes = {
    'Sat-A': ['Sat-B'],
    'Sat-B': ['Sat-A', 'Sat-C'],
    'Sat-C': ['Sat-B']
}

def validar_señal(sat_id, frecuencia, red_actual):
    """
    Verifica si la frecuencia elegida causa ruido con satélites adyacentes ya configurados.
    """
    adyacentes = interferencias_orbitantes.get(sat_id, [])
    for vecino in adyacentes:
        if vecino in red_actual and red_actual[vecino] == frecuencia:
            return False
    return True

# --- MOTOR DE BACKJUMPING DIRIGIDO ---

def coordinar_satelites(configuracion=None):
    """
    Asigna frecuencias de forma inteligente, saltando al origen del conflicto si falla.
    """
    if configuracion is None:
        configuracion = {}

    # Condición de éxito: Toda la constelación está configurada
    if len(configuracion) == len(satelites):
        print("\n[CONFIGURACIÓN EXITOSA] Constelación establecida:", configuracion)
        return configuracion

    # Identificamos el siguiente satélite a procesar
    sat_actual = satelites[len(configuracion)]

    for canal in canales:
        print(f"Probando {canal} en {sat_actual}...")

        if validar_señal(sat_actual, canal, configuracion):
            configuracion[sat_actual] = canal
            
            # Intentamos configurar el siguiente nivel de la red
            resultado = coordinar_satelites(configuracion)
            
            if resultado:
                return resultado
            
            # Si el camino falla, realizamos el salto
            print(f"  [!] Conflicto detectado en cascada. Saltando atrás desde {sat_actual}...")
            del configuracion[sat_actual]

    # Si se agotan las opciones, este nivel informa al anterior que la rama es inviable
    return None

# --- INICIO DEL PROTOCOLO DE COMUNICACIONES ---
print("--- Iniciando Sistema de Salto Atrás Dirigido ---")
coordinar_satelites()
