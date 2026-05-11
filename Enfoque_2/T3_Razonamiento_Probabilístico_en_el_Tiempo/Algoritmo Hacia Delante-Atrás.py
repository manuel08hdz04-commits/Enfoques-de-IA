'''
Algoritmo Hacia Delante-Atrás
Forward-Backward
'''

# ====================== ESTADOS ======================================

ESTADOS = ['soleado', 'lluvia']

# ====================== PROBABILIDADES INICIALES =====================

PI = {
    'soleado': 0.7,
    'lluvia': 0.3
}

# ====================== TRANSICIONES ================================

TRANSICION = {

    'soleado': {
        'soleado': 0.8,
        'lluvia': 0.2
    },

    'lluvia': {
        'soleado': 0.4,
        'lluvia': 0.6
    }
}

# ====================== EMISIONES ====================================

EMISION = {

    'soleado': {
        'paraguas': 0.1,
        'no_paraguas': 0.9
    },

    'lluvia': {
        'paraguas': 0.9,
        'no_paraguas': 0.1
    }
}

# ====================== FORWARD ======================================

def forward(observaciones):

    alpha = []

    # Inicialización
    alpha_0 = {}

    for estado in ESTADOS:
        alpha_0[estado] = (
            PI[estado] *
            EMISION[estado][observaciones[0]]
        )

    alpha.append(alpha_0)

    # Recursión
    for t in range(1, len(observaciones)):

        alpha_t = {}

        for estado_actual in ESTADOS:

            suma = 0

            for estado_prev in ESTADOS:

                suma += (
                    alpha[t-1][estado_prev] *
                    TRANSICION[estado_prev][estado_actual]
                )

            alpha_t[estado_actual] = (
                suma *
                EMISION[estado_actual][observaciones[t]]
            )

        alpha.append(alpha_t)

    return alpha

# ====================== BACKWARD =====================================

def backward(observaciones):

    beta = []

    # Inicialización
    beta_T = {}

    for estado in ESTADOS:
        beta_T[estado] = 1

    beta.insert(0, beta_T)

    # Recursión hacia atrás
    for t in range(len(observaciones)-2, -1, -1):

        beta_t = {}

        for estado_actual in ESTADOS:

            suma = 0

            for estado_sig in ESTADOS:

                suma += (
                    TRANSICION[estado_actual][estado_sig] *
                    EMISION[estado_sig][observaciones[t+1]] *
                    beta[0][estado_sig]
                )

            beta_t[estado_actual] = suma

        beta.insert(0, beta_t)

    return beta

# ====================== COMBINAR =====================================

def forward_backward(observaciones):

    alpha = forward(observaciones)
    beta = backward(observaciones)

    posterior = []

    for t in range(len(observaciones)):

        probs = {}

        total = 0

        for estado in ESTADOS:

            probs[estado] = (
                alpha[t][estado] *
                beta[t][estado]
            )

            total += probs[estado]

        # Normalizar
        for estado in probs:
            probs[estado] /= total

        posterior.append(probs)

    return posterior

# ====================== EJECUCIÓN ====================================

observaciones = [
    'paraguas',
    'paraguas',
    'no_paraguas'
]

resultado = forward_backward(observaciones)

print("\nForward-Backward:\n")

for t, probs in enumerate(resultado):

    print(f"Tiempo {t}:")
    print(probs)
    