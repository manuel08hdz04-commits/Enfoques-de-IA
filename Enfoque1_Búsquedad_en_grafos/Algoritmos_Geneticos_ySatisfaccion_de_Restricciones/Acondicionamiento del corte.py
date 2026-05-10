#¿Qué es el Acondicionamiento del Corte?
# La mayoría de los problemas de satisfacción de restricciones (CSP) son difíciles de resolver 
# (NP-duros) cuando tienen ciclos. Sin embargo, si un grafo es un árbol (no tiene ciclos), se puede 
# resolver de forma casi instantánea en tiempo lineal $O(nd^2)$.

# Cómo funciona:
# Identificación del Cutset: Buscamos un conjunto de nodos (en este caso uno solo) que, al ser 
# removidos o "fijados", transforman el resto del grafo en un árbol.
# Fijación de Variables: Elegimos una variable de corte y le asignamos un valor (congelamos su estado).
# Propagación y Resolución: Al fijar esa variable, sus vecinos ven sus opciones reducidas, y el resto 
# del problema se convierte en un árbol simple que se resuelve sin la complejidad de los ciclos.

import copy

# 1. Configuración de la Red
modos_frecuencia = ['Frecuencia-A', 'Frecuencia-B', 'Frecuencia-C']

# Grafo con un ANILLO DE RETROALIMENTACIÓN: 1-2-3-4-1
topologia_red = {
    'Nodo_1': ['Nodo_2', 'Nodo_4'],
    'Nodo_2': ['Nodo_1', 'Nodo_3'],
    'Nodo_3': ['Nodo_2', 'Nodo_4'],
    'Nodo_4': ['Nodo_3', 'Nodo_1']
}

# 2. ESTRATEGIA DE DESACOPLO
# Al fijar el 'Nodo_1', el anillo se abre y se convierte en una cadena simple.
nodo_corte = 'Nodo_1'
nodos_cadena = ['Nodo_2', 'Nodo_3', 'Nodo_4']

def configurar_cadena_lineal(indice, secuencia, red_actual, opciones):
    """Resuelve la configuración de los nodos restantes como una estructura lineal."""
    if indice >= len(secuencia):
        return True
        
    actual = secuencia[indice]
    
    for f in opciones[actual]:
        # Verificamos interferencia con vecinos ya configurados
        interferencia = False
        for adyacente in topologia_red[actual]:
            if adyacente in red_actual and red_actual[adyacente] == f:
                interferencia = True
                break
                
        if not interferencia:
            red_actual[actual] = f
            print(f"      [Cadena] -> {actual} configurado en {f}.")
            
            # Continuamos por la línea recta de la red
            if configurar_cadena_lineal(indice + 1, secuencia, red_actual, opciones):
                return True
                
            # Si hay fallo adelante, liberamos la frecuencia
            del red_actual[actual]
            
    return False

def estabilizador_por_corte():
    """
    Rompe ciclos de red fijando un nodo maestro y resolviendo el resto linealmente.
    """
    print("--- Iniciando Protocolo de Estabilización por Corte ---")
    print(f"[*] Punto de anclaje seleccionado para romper el ciclo: {nodo_corte}")
    
    opciones_base = {n: modos_frecuencia.copy() for n in topologia_red.keys()}
    
    # 3. Probamos cada frecuencia en el Nodo de Corte
    for f_maestra in modos_frecuencia:
        print(f"\n[Fase de Corte] Anclando {nodo_corte} a {f_maestra}...")
        
        configuracion = {nodo_corte: f_maestra}
        opciones_temporales = copy.deepcopy(opciones_base)
        
        # Al fijar el Nodo 1, restringimos a sus vecinos inmediatos
        error_de_red = False
        for vecino in topologia_red[nodo_corte]:
            if f_maestra in opciones_temporales[vecino]:
                opciones_temporales[vecino].remove(f_maestra)
                print(f"  -> Sincronizando {vecino}: Frecuencia {f_maestra} bloqueada.")
                if not opciones_temporales[vecino]:
                    error_de_red = True
                    
        if error_de_red:
            print(f"  [X] El anclaje en {f_maestra} colapsa la red vecina. Reintentando...")
            continue
            
        # 4. Resolvemos la topología restante (ahora es un árbol/línea)
        print(f"  [*] Ciclo abierto. Configurando estructura lineal restante: {nodos_cadena}")
        if configurar_cadena_lineal(0, nodos_cadena, configuracion, opciones_temporales):
            print(f"\n¡SISTEMA ESTABILIZADO! La red es consistente.")
            return configuracion
            
    print("\n[!] No se encontró una configuración estable.")
    return None

# --- EJECUCIÓN DEL SISTEMA ---
resultado_red = estabilizador_por_corte()

if resultado_red:
    print("\nEstado Final de la Red:")
    for nodo, frec in resultado_red.items():
        print(f"  {nodo} >> {frec}")