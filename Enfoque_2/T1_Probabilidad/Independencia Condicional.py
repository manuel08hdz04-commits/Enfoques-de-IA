#¿Qué es la Independencia Condicional?
# En el mundo real, las variables suelen estar relacionadas (si dices "dinero", es más probable que 
# digas "gratis"). Sin embargo, calcular todas las relaciones posibles entre miles de palabras es 
# computacionalmente imposible.La Independencia Condicional es la asunción de que, si ya conocemos 
# la clase (por ejemplo, sabemos que el correo es Spam), las palabras que aparecen son independientes 
# entre sí. 

# Esto nos permite simplificar la probabilidad conjunta como un simple producto:

# $$P(Palabra_1, Palabra_2 | Spam) = P(Palabra_1 | Spam) \times P(Palabra_2 | Spam)$$

# --- MOTOR DE CLASIFICACIÓN BASADO EN INDEPENDENCIA ---

def entrenar_modelo_seguridad(dataset):
    """
    Fase de Aprendizaje: Descompone el problema en probabilidades individuales.
    """
    total = len(dataset)
    conteo_clases = {"Estafa": 0, "Seguro": 0}
    # Guardamos frecuencias por clase
    frecuencias = {"Estafa": {}, "Seguro": {}}

    for clase, palabras in dataset:
        conteo_clases[clase] += 1
        for p in palabras:
            frecuencias[clase][p] = frecuencias[clase].get(p, 0) + 1

    # Convertimos conteos en probabilidades independientes P(Característica | Clase)
    modelo = {
        'prior': {clase: cant/total for clase, cant in conteo_clases.items()},
        'condicional': {"Estafa": {}, "Seguro": {}}
    }

    for clase in frecuencias:
        total_palabras_clase = sum(frecuencias[clase].values())
        for p, cant in frecuencias[clase].items():
            modelo['condicional'][clase][p] = cant / total_palabras_clase
            
    return modelo

def inferencia_bayesiana_independiente(modelo, sms):
    """
    Fase de Inferencia: Multiplica probabilidades asumiendo independencia.
    """
    resultados = {}

    for clase in ['Estafa', 'Seguro']:
        # Iniciamos con la probabilidad previa P(Clase)
        prob_total = modelo['prior'][clase]

        # ASUNCIÓN DE INDEPENDENCIA CONDICIONAL:
        # En lugar de buscar la frase entera, multiplicamos las partes.
        for palabra in sms:
            # P(SMS | Clase) = P(p1|Clase) * P(p2|Clase) * ...
            prob_p = modelo['condicional'][clase].get(palabra, 0.001) # Suavizado
            prob_total *= prob_p
            
        resultados[clase] = prob_total

    return max(resultados, key=resultados.get), resultados

# --- ESCENARIO DE PRUEBA ---
datos_historicos = [
    ('Estafa', ['premio', 'clic', 'urgente']),
    ('Estafa', ['dinero', 'urgente', 'clic']),
    ('Seguro', ['hola', 'casa', 'comida']),
    ('Seguro', ['nos', 'vemos', 'luego'])
]

# 1. Entrenamiento
brain_ia = entrenar_modelo_seguridad(datos_historicos)

# 2. Inferencia sobre un nuevo mensaje
nuevo_sms = ['urgente', 'clic']
veredicto, scores = inferencia_bayesiana_independiente(brain_ia, nuevo_sms)

print("--- ANÁLISIS DE INDEPENDENCIA CONDICIONAL ---")
print(f"Mensaje entrante: {nuevo_sms}")
print(f"Veredicto: {veredicto}")
print(f"Puntajes de confianza: {scores}")
