'''
Reconocimiento de "voz" simplificado con HMM + Viterbi
(SÍ pertenece a razonamiento probabilístico en el tiempo)
'''

# ====================== MODELOS ========================================

# Estados ocultos (fonemas simplificados)
ESTADOS = ['S1', 'S2', 'S3']

# Observaciones (sonidos simplificados)
OBSERVACIONES = ['a', 'o', 'i']

# Modelo para palabra "HOLA"
HMM_HOLA = {
    'PI': {'S1': 1.0, 'S2': 0.0, 'S3': 0.0},
    'TRANSICION': {
        'S1': {'S1': 0.1, 'S2': 0.9, 'S3': 0.0},
        'S2': {'S1': 0.0, 'S2': 0.1, 'S3': 0.9},
        'S3': {'S1': 0.0, 'S2': 0.0, 'S3': 1.0}
    },
    'EMISION': {
        'S1': {'o': 0.8, 'a': 0.1, 'i': 0.1},
        'S2': {'o': 0.2, 'a': 0.7, 'i': 0.1},
        'S3': {'o6': 0.1, 'a': 0.2, 'i': 0.7}
    }
}

# Modelo para palabra "ADIOS"
HMM_ADIOS = {
    'PI': {'S1': 1.0, 'S2': 0.0, 'S3': 0.0},
    'TRANSICION': {
        'S1': {'S1': 0.2, 'S2': 0.8, 'S3': 0.0},
        'S2': {'S1': 0.0, 'S2': 0.2, 'S3': 0.8},
        'S3': {'S1': 0.0, 'S2': 0.0, 'S3': 1.0}
    },
    'EMISION': {
        'S1': {'a': 0.7, 'o': 0.2, 'i': 0.1},
        'S2': {'i': 0.7, 'a': 0.2, 'o': 0.1},
        'S3': {'o': 0.7, 'a': 0.1, 'i': 0.2}
    }
}

# ====================== VITERBI ========================================

def viterbi(secuencia, modelo):
    estados = ESTADOS
    PI = modelo['PI']
    A = modelo['TRANSICION']
    B = modelo['EMISION']

    V = [{}]  # tabla
    path = {}

    # 🔹 Inicialización
    for estado in estados:
        V[0][estado] = PI[estado] * B[estado][secuencia[0]]
        path[estado] = [estado]

    # 🔹 Recursión
    for t in range(1, len(secuencia)):
        V.append({})
        new_path = {}

        for estado_actual in estados:
            (prob, estado_prev) = max(
                (V[t-1][e] * A[e][estado_actual] * B[estado_actual][secuencia[t]], e)
                for e in estados
            )

            V[t][estado_actual] = prob
            new_path[estado_actual] = path[estado_prev] + [estado_actual]

        path = new_path

    # 🔹 Resultado final
    (prob, estado_final) = max((V[-1][e], e) for e in estados)
    return prob, path[estado_final]

# ====================== RECONOCIMIENTO =================================

def reconocer(secuencia):
    prob_hola, _ = viterbi(secuencia, HMM_HOLA)
    prob_adios, _ = viterbi(secuencia, HMM_ADIOS)

    print("\nSecuencia:", secuencia)
    print("Probabilidad HOLA:", prob_hola)
    print("Probabilidad ADIOS:", prob_adios)

    if prob_hola > prob_adios:
        print("→ Palabra reconocida: HOLA")
    else:
        print("→ Palabra reconocida: ADIOS")

# ====================== EJECUCIÓN ======================================

# Simulación de "sonido"
secuencia = ['o', 'a', 'i'] #fonetica de "HOLA" (simplificada)
secuencia2 = ['a','i','o']

reconocer(secuencia)
reconocer(secuencia2)
