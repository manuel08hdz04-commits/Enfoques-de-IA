#¿Qué es un CSP?
# Un CSP (Constraint Satisfaction Problem) es un marco matemático donde el objetivo no es encontrar 
# una "ruta", sino encontrar un estado donde un conjunto de variables cumpla con todas las reglas 
# (restricciones) impuestas.

# Componentes clave:
# Variables ($X$): Los elementos a los que debemos asignar un valor (las torres).
# Dominios ($D$): Los valores posibles que puede tomar cada variable (las frecuencias disponibles).
# Restricciones ($C$): Las reglas que limitan qué valores pueden ir juntos (por ejemplo: "Torre A y 
# Torre B no pueden tener la misma frecuencia").

# Variables: Las antenas de telecomunicaciones que necesitan configuración
antenas = ['A', 'B', 'C']

# Dominio: Las bandas de frecuencia disponibles (Canales)
frecuencias_disponibles = ['Banda-700MHz', 'Banda-850MHz']

# Restricciones: Mapa de adyacencia (Antenas que causan interferencia si usan lo mismo)
interferencias = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

def verificar_interferencia(antena_focal, frecuencia_propuesta, configuracion_actual):
    """
    Comprueba si asignar una frecuencia a una antena rompe las reglas de proximidad.
    """
    # Revisamos todas las antenas que tienen restricción con la antena actual
    vecinos_criticos = interferencias.get(antena_focal, [])
    
    for vecino in vecinos_criticos:
        # Si el vecino ya tiene una frecuencia asignada...
        if vecino in configuracion_actual:
            # ...y es la misma frecuencia que queremos usar, hay interferencia (Invalido)
            if configuracion_actual[vecino] == frecuencia_propuesta:
                print(f"  [!] Conflicto detectado: {antena_focal} y {vecino} colisionan en {frecuencia_propuesta}")
                return False
                
    return True

# --- Ejemplo de Lógica de Asignación ---
asignaciones = {}
print("--- Iniciando Configuración de Red CSP ---")

for torre in antenas:
    for banda in frecuencias_disponibles:
        print(f"Probando {banda} en Antena {torre}...")
        if verificar_interferencia(torre, banda, asignaciones):
            asignaciones[torre] = banda
            print(f"  [+] Antena {torre} configurada exitosamente.")
            break

print("\nPlan de Frecuencias Finalizado:")
for torre, banda in asignaciones.items():
    print(f"Torre {torre} -> {banda}")