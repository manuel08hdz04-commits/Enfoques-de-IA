#¿Qué es la Propagación de Restricciones (AC-3)?
# El algoritmo AC-3 (Arc Consistency Algorithm #3) es una técnica de pre-procesamiento que se utiliza 
# para limpiar los dominios de las variables antes (o durante) la búsqueda. Mientras que el Forward 
# Checking solo mira los vecinos de la variable actual, el AC-3 propaga el efecto de una restricción 
# a través de toda la red.

# Cómo funciona:
# Consistencia de Arco: Se asegura de que para cada valor en el dominio de una variable $X$, exista 
# al menos un valor en el dominio de la variable vecina $Y$ que permita cumplir la restricción.
# Efecto Dominó: Si eliminamos un valor de una terminal porque no encaja con su vecina, esa 
# eliminación podría causar que otras terminales conectadas también tengan que eliminar valores. 
# El algoritmo repite el proceso hasta que los dominios estén "estabilizados".
# Resultado: No siempre resuelve el problema por sí solo, pero reduce drásticamente las opciones, 
# dejando los dominios listos para que un algoritmo de Backtracking termine el trabajo casi 
# instantáneamente.

# Terminales del aeropuerto
terminales = ['Norte (A)', 'Central (B)', 'Sur (C)']

# Protocolos de seguridad disponibles
protocolos = ['Escaneo-Bio', 'Escaneo-RayosX']

# Conexiones: Terminales que deben mantener protocolos distintos para evitar cuellos de botella
conexiones_seguridad = {
    'Norte (A)': ['Central (B)'],
    'Central (B)': ['Norte (A)', 'Sur (C)'],
    'Sur (C)': ['Central (B)']
}

def algoritmo_ac3_seguridad():
    """
    Propaga las restricciones para asegurar la consistencia entre terminales conectadas.
    """
    # Inicializamos cada terminal con todos los protocolos disponibles
    hoja_dominios = {t: list(protocolos) for t in terminales}

    print(f"--- Iniciando Depuración AC-3 ---")
    print(f"Dominios iniciales: {hoja_dominios}\n")

    # Flag para mantener el ciclo mientras ocurran cambios (propagación)
    hubo_cambios = True
    
    while hubo_cambios:
        hubo_cambios = False
        
        for t_actual in terminales:
            # Revisamos la consistencia con cada terminal conectada (arco)
            for t_vecina in conexiones_seguridad[t_actual]:
                
                # Evaluamos cada protocolo en el dominio de la terminal actual
                for p_actual in hoja_dominios[t_actual][:]:
                    
                    # REGLA DE CONSISTENCIA:
                    # ¿Existe algún protocolo en la terminal vecina que sea diferente al actual?
                    # Si todos los protocolos de la vecina son iguales al actual, el actual es inválido.
                    if all(p_actual == p_vecino for p_vecino in hoja_dominios[t_vecina]):
                        hoja_dominios[t_actual].remove(p_actual)
                        hubo_cambios = True
                        print(f"  [!] Inconsistencia: Eliminando {p_actual} de {t_actual} por conflicto con {t_vecina}")

    print("\n--- Resultado de la Propagación ---")
    print(f"Opciones finales consistentes: {hoja_dominios}")
    return hoja_dominios

# --- EJECUCIÓN DEL SISTEMA ---
algoritmo_ac3_seguridad()
