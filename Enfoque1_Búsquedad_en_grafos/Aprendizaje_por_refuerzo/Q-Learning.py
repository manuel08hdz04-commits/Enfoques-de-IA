#¿Qué es el Q-Learning?
# El Q-Learning es un algoritmo de aprendizaje por refuerzo off-policy. Su objetivo es aprender una 
# política que le diga a un agente qué acción tomar bajo qué circunstancias. No necesita un modelo del 
# entorno y puede manejar problemas con transiciones estocásticas y recompensas demoradas.

# Los componentes del aprendizaje:
# La Tabla Q: Es la "base de datos de calidad" del agente. Para cada estado y cada acción, guarda un 
# valor numérico (Q) que representa la recompensa total esperada.
# La Ecuación de Bellman (Actualización): Es la fórmula que permite al agente aprender de sus 
# errores.$$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
# Epsilon-Greedy ($\epsilon$): El equilibrio entre explorar (probar rutas nuevas) y explotar (usar la 
# mejor ruta conocida).

import random

# --- CONFIGURACIÓN DEL ALMACÉN (Grafo de estados) ---
# Los nodos son ubicaciones y las listas son conexiones posibles.
almacen = {
    'Entrada': ['Pasillo_1', 'Pasillo_2'],
    'Pasillo_1': ['Muelle_Carga', 'Estanteria_A'],
    'Pasillo_2': ['Salida_Emergencia'],
    'Muelle_Carga': [], # OBJETIVO
    'Estanteria_A': ['Muelle_Carga'],
    'Salida_Emergencia': []
}

objetivo = 'Muelle_Carga'

# --- INICIALIZACIÓN DE LA TABLA Q ---
# Q[estado][accion] inicializado en 0.0
Q = {estado: {accion: 0.0 for accion in almacen[estado]} for estado in almacen}

# PARÁMETROS
alfa = 0.2    # Tasa de aprendizaje
gamma = 0.9   # Factor de descuento (valor del futuro)
epsilon = 0.3 # Probabilidad de exploración

def obtener_recompensa(estado):
    """Refuerzo: 100 por llegar, -1 por cada paso para incentivar rapidez."""
    return 100 if estado == objetivo else -1

def elegir_maniobra(estado):
    """Estrategia Epsilon-Greedy."""
    if not almacen[estado]: return None
    
    # Exploración (Azar)
    if random.random() < epsilon:
        return random.choice(almacen[estado])
    # Explotación (Conocimiento)
    return max(Q[estado], key=Q[estado].get)

def entrenar_robot(ciclos=500):
    """Proceso de aprendizaje mediante interacción."""
    for _ in range(ciclos):
        actual = 'Entrada'
        
        while actual != objetivo:
            accion = elegir_maniobra(actual)
            if not accion: break
            
            proximo = accion
            recompensa = obtener_recompensa(proximo)
            
            # Predicción del mejor valor futuro
            max_futuro = max(Q[proximo].values()) if Q[proximo] else 0
            
            # ACTUALIZACIÓN DE BELLMAN
            # Ajustamos el valor actual basándonos en la recompensa + potencial futuro
            Q[actual][accion] += alfa * (recompensa + gamma * max_futuro - Q[actual][accion])
            
            actual = proximo

# --- EJECUCIÓN DEL ENTRENAMIENTO ---
entrenar_robot()

print("--- TABLA DE CONOCIMIENTO (Q-VALUES) ---")
for estado, acciones in Q.items():
    if acciones:
        print(f"En {estado}: {acciones}")

# --- VALIDACIÓN DE LA RUTA ÓPTIMA ---
def test_ruta():
    paso = 'Entrada'
    ruta = [paso]
    while paso != objetivo:
        if not Q[paso]: break
        paso = max(Q[paso], key=Q[paso].get) # Elegir siempre lo mejor
        ruta.append(paso)
    return ruta

print("\n" + "="*50)
print(f" RUTA ÓPTIMA APRENDIDA: {' -> '.join(test_ruta())} ")
print("="*50)