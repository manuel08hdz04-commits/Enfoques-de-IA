#¿Qué es la Regla de Bayes?
# La Regla de Bayes es la fórmula matemática que nos permite actualizar nuestras creencias a medida 
# que aparece nueva evidencia. Es el motor que permite a la IA aprender de la experiencia. 
# Su forma clásica es:$$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$$

# Los 4 pilares de la fórmula:
# Prior ($P(A)$): Nuestra creencia inicial antes de ver la prueba.
# Likelihood ($P(B|A)$): La probabilidad de que la prueba dé positivo si realmente tienes la condición.
# Evidencia ($P(B)$): La probabilidad total de que la prueba dé positivo (incluyendo aciertos y 
# errores).
# Posterior ($P(A|B)$): La probabilidad actualizada que buscamos.

# --- MOTOR DE INFERENCIA BAYESIANA ---

def motor_diagnostico_bayes(prior_enfermedad, sensibilidad, tasa_falso_positivo):
    """
    Calcula la probabilidad real (Posterior) tras un test positivo.
    """
    # 1. Probabilidad de estar sano
    prior_sano = 1.0 - prior_enfermedad
    
    # 2. El denominador: P(Evidencia)
    # Suma de Verdadaderos Positivos + Falsos Positivos
    verdaderos_positivos = sensibilidad * prior_enfermedad
    falsos_positivos = tasa_falso_positivo * prior_sano
    prob_total_positivo = verdaderos_positivos + falsos_positivos
    
    # 3. Aplicación de la Regla de Bayes
    prob_real_enfermo = verdaderos_positivos / prob_total_positivo
    
    return {
        "riesgo_real": prob_real_enfermo,
        "ruido_falsos_pos": falsos_positivos,
        "aciertos_reales": verdaderos_positivos
    }

# --- ESCENARIO: Test de Enfermedad Rara ---
prevalencia = 0.001   # 1 de cada 1000 personas la tiene (0.1%)
precision_test = 0.99 # El test acierta el 99% de las veces
error_test = 0.05     # El test falla el 5% de las veces en personas sanas

# Ejecución
analisis = motor_diagnostico_bayes(prevalencia, precision_test, error_test)

print("--- REPORTE DE PROBABILIDAD MÉDICA ---")
print(f"Resultado del Test: POSITIVO")
print(f"Probabilidad Posterior: {analisis['riesgo_real']*100:.2f}%")

# Explicación de la IA
print("\n--- NOTA DEL ASISTENTE ---")
if analisis['riesgo_real'] < 0.20:
    print("Aunque el test dio positivo, la enfermedad es tan rara que es")
    print(f"casi {int(analisis['ruido_falsos_pos']/analisis['aciertos_reales'])} veces más probable que sea un falso positivo.")


    