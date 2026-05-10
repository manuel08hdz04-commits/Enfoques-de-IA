#¿Qué es la Búsqueda de Mínimos Conflictos?
#A diferencia de los algoritmos de búsqueda sistemática (como el Backtracking), que construyen la 
# solución paso a paso, los Mínimos Conflictos son una forma de Búsqueda Local. Comienza con una 
# asignación completa (aunque tenga errores) y la repara iterativamente.

#Cómo funciona:

#Asignación Inicial: Se asigna un valor aleatorio a todas las variables desde el principio.

#Selección de Variable: Se elige al azar una variable que esté causando algún conflicto (por ejemplo, 
# dos médicos en el mismo turno).

#Minimización: Para esa variable, se elige el nuevo valor que minimice el número de conflictos con 
# sus vecinos.

#Eficiencia: Es asombrosamente rápido para problemas grandes (como el de las n-reinas) porque se 
# enfoca solo en "reparar" lo que está roto en lugar de reconstruir todo desde cero.

import random

# Personal médico asignado a guardias
medicos = ['Dr. A', 'Dra. B', 'Dr. C']

# Turnos disponibles (Frecuencias/Colores)
turnos = ['Mañana', 'Noche']

# Restricciones de contacto: Médicos que no pueden compartir el mismo turno
proximidad_critica = {
    'Dr. A': ['Dra. B'],
    'Dra. B': ['Dr. A', 'Dr. C'],
    'Dr. C': ['Dra. B']
}

def optimizar_guardias(max_intentos=50):
    """
    Algoritmo de Mínimos Conflictos: Repara una agenda con errores iniciales.
    """
    # Paso 1: Generamos una agenda inicial totalmente aleatoria
    agenda = {m: random.choice(turnos) for m in medicos}
    print(f"--- Plan de Guardias Inicial (con posibles conflictos): {agenda} ---")

    for i in range(max_intentos):
        # Identificamos quiénes tienen conflicto actualmente
        lista_conflictos = []
        for m in medicos:
            for colega in proximidad_critica[m]:
                if agenda[m] == agenda[colega]:
                    lista_conflictos.append(m)
                    break # Con un conflicto basta para marcar al médico

        # Si no hay conflictos, hemos terminado
        if not lista_conflictos:
            print(f"\n¡ÉXITO! Agenda optimizada en {i} iteraciones.")
            print(f"Resultado final: {agenda}")
            return agenda

        # Paso 2: Elegimos a un médico con conflicto al azar para reasignarlo
        medico_a_mover = random.choice(lista_conflictos)
        print(f"Iteración {i}: Resolviendo conflicto de {medico_a_mover}")

        # Paso 3: Buscamos el turno que le cause MENOS problemas con sus colegas
        # Esta es la esencia de 'Mínimos Conflictos'
        agenda[medico_a_mover] = min(turnos, key=lambda t: sum(
            1 for colega in proximidad_critica[medico_a_mover] 
            if agenda.get(colega) == t
        ))

        print(f"  -> Nuevo estado de la red: {agenda}")

    print("\nLímite de intentos alcanzado. La agenda aún presenta conflictos.")
    return agenda

# --- EJECUCIÓN DEL SISTEMA ---
optimizar_guardias()