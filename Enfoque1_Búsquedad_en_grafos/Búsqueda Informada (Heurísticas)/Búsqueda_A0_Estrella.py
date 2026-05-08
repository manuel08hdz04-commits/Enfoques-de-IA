#¿Qué es la Búsqueda AO*?
# El algoritmo AO* se utiliza para explorar Grafos AND/OR, que son estructuras donde un problema se 
# divide en sub-problemas. A diferencia del A* estándar, que busca una ruta única, el AO* busca un 
# hiper-grafo o árbol de solución.

# Cómo funciona:
# Nodos OR: Representan una elección. Solo necesitas resolver una de las opciones disponibles para 
# completar la tarea. Se elige la de menor costo ($min$).
# Nodos AND: Representan tareas complejas que deben descomponerse. Para completar la tarea, todas 
# las sub-tareas deben ser resueltas. El costo es la suma de los hijos ($sum$).
# Es fundamental en Inteligencia Artificial para la resolución de problemas mediante descomposición y 
# en sistemas expertos.

# Definición del flujo de trabajo (Grafo AND/OR)
# 'DIVERGENTE' (OR): Elegir la mejor alternativa.
# 'CONJUNTO' (AND): Requisitos obligatorios simultáneos.
flujo_ingenieria = {
    'A': {'clase': 'DIVERGENTE', 'subtareas': ['B', 'C']},
    'B': {'clase': 'CONJUNTO',   'subtareas': ['D', 'E']}, # D y E son críticos para B
    'C': {'clase': 'DIVERGENTE', 'subtareas': ['F']},
    # Actividades base (ya cuantificadas)
    'D': {'clase': 'DIVERGENTE', 'subtareas': []},
    'E': {'clase': 'DIVERGENTE', 'subtareas': []},
    'F': {'clase': 'DIVERGENTE', 'subtareas': []}
}

# Estimación de inversión por cada actividad base
presupuesto_estimado = {
    'A': 10, 'B': 8, 'C': 5, 
    'D': 2,  'E': 3, 'F': 6
}

def optimizar_recursos_ao(proyectos, costos, hito_actual):
    """
    Algoritmo AO*: Calcula el costo de resolución basándose en dependencias AND/OR.
    """
    # Verificamos los detalles de la tarea en el flujo
    datos_hito = proyectos.get(hito_actual, {'clase': 'DIVERGENTE', 'subtareas': []})
    
    # Caso base: Si la tarea no tiene dependencias, retornamos su presupuesto asignado
    if not datos_hito['subtareas']:
        print(f"  [Actividad Finalizada] '{hito_actual}' costeada en: {costos[hito_actual]}")
        return costos[hito_actual]
        
    print(f"Analizando viabilidad de '{hito_actual}' (Estructura: {datos_hito['clase']})")
    evaluacion_hijos = []
    
    # Exploración recursiva de todas las dependencias
    for sub_tarea in datos_hito['subtareas']:
        evaluacion_hijos.append(optimizar_recursos_ao(proyectos, costos, sub_tarea))
        
    if datos_hito['clase'] == 'CONJUNTO':
        # Lógica AND: Se deben financiar todas las subtareas + gasto de gestión (+1)
        total_inversion = sum(evaluacion_hijos) + 1
        print(f"  -> Requisito '{hito_actual}' (CONJUNTO): Suma de partes. Inversión: {total_inversion}")
        return total_inversion
        
    elif datos_hito['clase'] == 'DIVERGENTE':
        # Lógica OR: Se selecciona la opción más económica + gasto de gestión (+1)
        total_inversion = min(evaluacion_hijos) + 1
        print(f"  -> Opción '{hito_actual}' (DIVERGENTE): Selección mínima. Inversión: {total_inversion}")
        return total_inversion

# --- INICIO DEL CÁLCULO DE PRESUPUESTO ---
print("--- Ejecutando Motor de Optimización de Proyectos AO* ---")
inversion_optima = optimizar_recursos_ao(flujo_ingenieria, presupuesto_estimado, 'B')
print(f"\nLa inversión mínima para completar el proyecto raíz 'B' es de: {inversion_optima} unidades.")