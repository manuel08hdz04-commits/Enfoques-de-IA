'''
MDP - PROCESO DE DECISIÓN DE MARKOV

Modelo para tomar decisiones en situaciones con incertidumbre.

Ejemplo: decidir qué hacer durante el día
(Trabajar o Descansar)
'''

# ====================== CLASE MDP ======================================

class MDP:
    def __init__(self, estados, acciones, transiciones, recompensas, gamma=0.9):
        self.estados = estados                # Lista de estados
        self.acciones = acciones              # Lista de acciones
        self.transiciones = transiciones      # Probabilidades
        self.recompensas = recompensas        # Ganancias
        self.gamma = gamma                    # Factor de descuento

    # Mostrar información del modelo
    def mostrar(self):
        print("Estados:", self.estados)
        print("Acciones:", self.acciones)
        print("Gamma:", self.gamma)


# ====================== EJEMPLO VIDA REAL ==============================

estados = ["Descansar", "Trabajar"]

acciones = ["quedarse"]

# Probabilidad de cambiar de estado
transiciones = {
    "Descansar": {"quedarse": {"Descansar": 0.7, "Trabajar": 0.3}},
    "Trabajar": {"quedarse": {"Descansar": 0.4, "Trabajar": 0.6}}
}

# Recompensas (beneficios)
recompensas = {
    "Descansar": {"quedarse": {"Descansar": 2, "Trabajar": 5}},
    "Trabajar": {"quedarse": {"Descansar": 3, "Trabajar": 6}}
}

# Crear modelo MDP
mdp = MDP(estados, acciones, transiciones, recompensas)

# ====================== EJECUCIÓN ======================================

print("\n[29 - MDP:]")
mdp.mostrar()
