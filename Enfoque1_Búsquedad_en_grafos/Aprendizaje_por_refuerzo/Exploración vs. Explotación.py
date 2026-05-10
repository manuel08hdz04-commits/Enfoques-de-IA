#El Gran Dilema: Exploración vs. Explotación Este es el núcleo de la toma de decisiones bajo 
# incertidumbre. Si una IA solo hace lo que ya sabe que funciona, se estanca (podría ignorar un tesoro 
# mayor a la vuelta de la esquina). Si solo prueba cosas nuevas, nunca acumula recompensas.

# Exploración (Probar): El agente elige una acción al azar para descubrir información sobre el entorno. 
# Es vital al principio del aprendizaje.

# Explotación (Usar): El agente elige la mejor acción según su conocimiento actual (el valor $Q$ más 
# alto). Es vital para maximizar la ganancia final.

import random

# --- EL ENTORNO (Zonas de Minería) ---
# Cada conexión tiene una recompensa inmediata (cantidad de mineral)
minas = {
    'Base': {'Sector_Norte': 10, 'Sector_Sur': 50},
    'Sector_Norte': {'Cueva_Alfa': 20, 'Cueva_Beta': 100},
    'Sector_Sur': {'Tunel_Oscuro': 30},
    'Cueva_Alfa': {},
    'Cueva_Beta': {},
    'Tunel_Oscuro': {}
}

# --- PARÁMETROS ---
epsilon = 0.3  # 30% del tiempo exploramos (azar), 70% explotamos (lo mejor)
alfa = 0.1     # Tasa de aprendizaje
episodios = 15

# Inicializamos el conocimiento del Dron (Valores Q)
Q = {nodo: {vecino: 0.0 for vecino in minas[nodo]} for nodo in minas}

def elegir_maniobra(estado):
    """Implementación de la estrategia Epsilon-Greedy."""
    posibilidades = list(minas[estado].keys())
    if not posibilidades: return None

    # ¿Explorar o Explotar?
    if random.random() < epsilon:
        # EXPLORACIÓN: Curiosidad por lo desconocido
        return random.choice(posibilidades)
    else:
        # EXPLOTACIÓN: Ir a lo seguro (el valor Q más alto)
        # Si todos son 0, max() devuelve el primero
        return max(Q[estado], key=Q[estado].get)

# --- CICLO DE APRENDIZAJE ---
print(f"--- Iniciando Misiones con Epsilon={epsilon} ---")

for i in range(episodios):
    actual = 'Base'
    camino = []
    
    while minas[actual]:
        accion = elegir_maniobra(actual)
        recompensa = minas[actual][accion]
        
        # ACTUALIZACIÓN DE CONOCIMIENTO (Regla Delta)
        # Ajustamos nuestra creencia (Q) hacia la recompensa real obtenida
        Q[actual][accion] += alfa * (recompensa - Q[actual][accion])
        
        camino.append(f"{actual}->{accion}")
        actual = accion

    print(f"Misión {i+1:02d}: {' | '.join(camino)}")

print("\n" + "="*50)
print(" MAPA DE CONOCIMIENTO FINAL (Valores Q) ")
print("="*50)
for nodo, acciones in Q.items():
    if acciones:
        print(f" En {nodo}: {acciones}")
        