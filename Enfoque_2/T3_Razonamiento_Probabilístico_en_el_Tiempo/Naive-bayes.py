'''
Aprendizaje Bayesiano (Naive Bayes)
Clasificación probabilística basada en datos
'''

# ====================== DATOS ==========================================

# Dataset: (clima, temperatura) → actividad
datos = [
    ('soleado', 'calor', 'no'),
    ('soleado', 'calor', 'no'),
    ('nublado', 'calor', 'si'),
    ('lluvia', 'templado', 'si'),
    ('lluvia', 'frio', 'si'),
    ('lluvia', 'frio', 'no'),
    ('nublado', 'frio', 'si'),
    ('soleado', 'templado', 'no'),
    ('soleado', 'frio', 'si'),
    ('lluvia', 'templado', 'si')
]
#"si" y "no" es solo la clase, lo podemos tomar como "si está soleado y hace calor, no hago una actividad"
#las clases o categorias es lo que este modelo aprende a predecir


# ====================== ENTRENAMIENTO ================================

def entrenar(datos): #el modelo aprende probabilidades a partir de frecuencias
    total = len(datos)
    clases = {}
    
    for clima, temp, clase in datos:
        if clase not in clases:
            clases[clase] = {
                'count': 0,
                'clima': {},
                'temp': {}
            }
        
        clases[clase]['count'] += 1
        
        # Contar clima
        clases[clase]['clima'][clima] = clases[clase]['clima'].get(clima, 0) + 1
        
        # Contar temperatura
        clases[clase]['temp'][temp] = clases[clase]['temp'].get(temp, 0) + 1

    return clases, total

# ====================== CLASIFICACIÓN ================================

def clasificar(modelo, total, clima, temp):
    clases = modelo
    resultados = {}

    for clase in clases:
        # Probabilidad a priori
        P_clase = clases[clase]['count'] / total
        
        # Probabilidades condicionales
        P_clima = clases[clase]['clima'].get(clima, 0.0001) / clases[clase]['count']
        P_temp = clases[clase]['temp'].get(temp, 0.0001) / clases[clase]['count']
        
        # Naive Bayes (independencia)
        prob = P_clase * P_clima * P_temp
        resultados[clase] = prob

    return resultados

# ====================== EJECUCIÓN ======================================

modelo, total = entrenar(datos)

# Nuevo caso
entrada = ('soleado', 'frio')

resultados = clasificar(modelo, total, entrada[0], entrada[1])

print("\nEntrada:", entrada)
print("Probabilidades:", resultados)

# Decisión final
mejor = max(resultados, key=resultados.get)
print("Clasificación:", mejor)

