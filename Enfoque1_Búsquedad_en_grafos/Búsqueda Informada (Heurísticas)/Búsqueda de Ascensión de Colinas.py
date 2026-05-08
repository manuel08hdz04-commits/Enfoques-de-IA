#¿Qué es la Ascensión de Colinas (Hill Climbing)?
#Es un algoritmo de optimización local que pertenece a la familia de búsqueda informada. Se le conoce 
# como un algoritmo "voraz" que no mantiene un historial de búsqueda ni retrocede 
# (no hace backtracking).

#Cómo funciona:
# El algoritmo comienza en un estado aleatorio o inicial y examina a sus vecinos inmediatos.
# Si encuentra un vecino con un valor mejor (en este caso, un valor más bajo de distancia a la meta), 
# se mueve hacia él inmediatamente.
# El gran riesgo: Si llega a un punto donde todos sus vecinos son peores que su posición actual, se 
# detiene y declara que ha llegado a la "cima".
# Esto puede causar que el algoritmo se quede atrapado en un Máximo Local (una colina pequeña que no 
# es la verdadera montaña que buscamos) o en una Meseta.

# Mapa de crestas y senderos (Grafo de elevaciones)
terreno_montañoso = {
    'Inicio': ['A', 'B'],
    'A': ['C', 'D'],      # El sendero 'A' parece prometedor pero es una trampa
    'B': ['E'],           # El sendero 'B' es el camino a la cumbre real
    'C': [], 
    'D': ['F'],           # 'D' es la cima de una colina menor (Máximo Local)
    'E': ['Z'],           
    'F': [],
    'Z': []               # La Cumbre Principal (Máximo Global)
}

# Lecturas del Altímetro (Heurística): Distancia vertical restante a la meta
# Buscamos reducir este valor a 0.
lectura_altimetro = {
    'Inicio': 10,
    'A': 7,    
    'B': 9,    
    'C': 8,
    'D': 4,    # Falsa cumbre: ningún vecino es menor a 4
    'F': 5,
    'E': 3,
    'Z': 0  
}

def escalar_montaña_ciega(mapa, sensor, posicion_base):
    """
    Algoritmo Hill Climbing: Solo avanza si el siguiente paso reduce la altitud restante.
    """
    print(f"--- Iniciando Expedición desde el campamento '{posicion_base}' ---")
    
    ruta_ascenso = [posicion_base]
    punto_actual = posicion_base

    while True:
        valor_gps = sensor[punto_actual]
        print(f"\nUbicación: {punto_actual} | Pendiente restante: {valor_gps}m")
        
        # Condición de victoria: Llegamos al punto más alto (valor 0)
        if valor_gps == 0:
            print("¡OBJETIVO LOGRADO! Hemos alcanzado la Cumbre Principal.")
            print(f"Ruta de ascenso: {' -> '.join(ruta_ascenso)}")
            return True

        opciones_paso = mapa.get(punto_actual, [])
        
        # Si no hay más senderos, estamos en un pico aislado
        if not opciones_paso:
            print("Ruta cortada. ¡Atrapados en un risco sin salida!")
            return False

        # Exploración del entorno inmediato para encontrar el MEJOR paso
        mejor_opcion = None
        menor_distancia = float('inf') 
        
        for candidato in opciones_paso:
            distancia_vecino = sensor.get(candidato, float('inf'))
            print(f"  ? Evaluando sendero '{candidato}' (Distancia estimada: {distancia_vecino}m)")
            
            if distancia_vecino < menor_distancia:
                menor_distancia = distancia_vecino
                mejor_opcion = candidato

        # LÓGICA CRÍTICA: Si el mejor paso disponible no mejora mi posición actual, me detengo.
        if menor_distancia >= valor_gps:
            print(f"\n[!] AVISO: El mejor paso ('{mejor_opcion}') es cuesta arriba o igual.")
            print(f"El montañista se detiene en '{punto_actual}' creyendo que es la cima.")
            print(f"Resultado: Atrapado en Máximo Local. Ruta final: {ruta_ascenso}")
            return False
            
        # El algoritmo es voraz: toma la mejor opción y olvida el resto
        print(f"-> Avanzando con determinación hacia '{mejor_opcion}'...")
        punto_actual = mejor_opcion
        ruta_ascenso.append(punto_actual)

# --- PRUEBA DE CAMPO ---
escalar_montaña_ciega(terreno_montañoso, lectura_altimetro, 'Inicio')