#¿Qué es el Aprendizaje por Refuerzo Activo?
#A diferencia del refuerzo pasivo (donde la IA es una simple espectadora), en el Aprendizaje Activo, 
# el agente tiene el control total. La IA debe decidir constantemente entre dos impulsos:

#Explotación: Usar los caminos que ya sabe que funcionan para obtener recompensas rápido.

#Exploración: Probar caminos desconocidos para ver si hay una recompensa mayor escondida.

#En el aprendizaje activo, el agente interactúa con el entorno, recibe retroalimentación y actualiza 
# su propia política de decisión en tiempo real.

from collections import deque

# --- EL MAPA DE LA MAZMORRA ---
mazmorra = {
    'Entrada': ['Pasillo_A', 'Pasillo_B'],
    'Pasillo_A': ['Fosa_Lava', 'Cámara_Secreta'],
    'Pasillo_B': ['Biblioteca'],
    'Fosa_Lava': [],
    'Cámara_Secreta': ['Tesoro'],
    'Biblioteca': ['Tesoro'],
    'Tesoro': []
}

meta = 'Tesoro'

# --- MEMORIA DE EXPERIENCIA (Q-Table simplificada) ---
# Almacena el valor de utilidad que el agente le otorga a cada sala.
experiencia = {sala: 0 for sala in mazmorra}

def explorar_mazmorra(inicio, modo_entrenamiento=True):
    """
    El agente recorre la mazmorra. Si encuentra el tesoro, 
    refuerza positivamente todos los pasos que lo llevaron ahí.
    """
    cola = deque([[inicio]]) 
    visitados = set()
    pasos_dados = []
    
    while cola:
        camino = cola.popleft()
        sala_actual = camino[-1]
        pasos_dados.append(sala_actual)
        
        if sala_actual == meta:
            # REFUERZO ACTIVO: El agente aprende que este camino fue exitoso.
            if modo_entrenamiento:
                for sala in camino:
                    experiencia[sala] += 1
            return camino, pasos_dados
        
        if sala_actual not in visitados:
            visitados.add(sala_actual)
            
            # EL CORAZÓN DEL APRENDIZAJE ACTIVO:
            # El agente ordena sus opciones basadas en lo que ha aprendido (experiencia).
            opciones = mazmorra[sala_actual]
            opciones_priorizadas = sorted(
                opciones,
                key=lambda x: experiencia[x],
                reverse=True # Prioriza salas con mayor valor de refuerzo
            )
            
            for siguiente in opciones_priorizadas:
                nuevo_camino = list(camino)
                nuevo_camino.append(siguiente)
                cola.append(nuevo_camino)
    
    return None, pasos_dados

# --- CICLO DE APRENDIZAJE ---
print("--- ENTRENAMIENTO DEL EXPLORADOR ---")
for i in range(1, 4):
    exito, recorrido = explorar_mazmorra('Entrada')
    print(f"Intento {i}: Encontró el Tesoro vía {exito}")

# --- DEMOSTRACIÓN FINAL ---
print("\n" + "="*50)
print(" COMPORTAMIENTO DEL AGENTE REFORZADO ")
print("="*50)
ruta_final, bitacora = explorar_mazmorra('Entrada', modo_entrenamiento=False)

print(f"Instinto del agente (Recorrido): {' -> '.join(bitacora)}")
print(f"Camino Óptimo aprendido: {' -> '.join(ruta_final)}")

print("\nMapa de Valor (Refuerzo):")
for sala, valor in experiencia.items():
    barra = "★" * valor
    print(f" {sala.ljust(15)} | {valor} {barra}")
    