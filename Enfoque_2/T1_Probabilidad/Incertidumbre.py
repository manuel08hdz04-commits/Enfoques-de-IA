#¿Por qué la IA necesita Probabilidad?
# En el mundo real, los agentes casi nunca tienen acceso a la verdad absoluta. Los sensores tienen 
# ruido, las cámaras se empañan y los radares fallan. La Inferencia Bayesiana permite a la IA 
# actualizar lo que cree a medida que recibe nueva evidencia.

# Los componentes del razonamiento bayesiano:
# Prior ($P(H)$): Lo que sabemos antes de mirar el sensor. (¿Es común ver peatones en esta carretera?)
# .Likelihood ($P(E|H)$): Qué tan confiable es el sensor. (Si hay alguien, ¿qué tan probable es que 
# el sensor pite?).
# Posterior ($P(H|E)$): La nueva realidad calculada tras combinar nuestra experiencia previa con la 
# nueva evidencia.

# --- MOTOR DE INFERENCIA DE SEGURIDAD VIAL ---

def sistema_decision_bayesian(prior_peaton, prob_fallo_sensor):
    """
    Calcula la probabilidad real de una amenaza tras una detección.
    """
    # 1. DEFINICIÓN DEL ESCENARIO
    p_h = prior_peaton                # Probabilidad previa (Prior)
    p_not_h = 1.0 - p_h               # Probabilidad de que no haya nadie
    
    # 2. ESPECIFICACIONES DEL RADAR (Likelihoods)
    # Sensibilidad: P(Detección | Peatón)
    p_e_given_h = 0.90 
    
    # Especificidad negativa (Falso Positivo): P(Detección | Aire/Niebla)
    # Este es el ruido del sensor.
    p_e_given_not_h = prob_fallo_sensor 

    # 3. CÁLCULO DE LA PROBABILIDAD TOTAL DE ALERTA P(E)
    # Es la suma de detecciones reales y detecciones erróneas.
    p_e = (p_e_given_h * p_h) + (p_e_given_not_h * p_not_h)

    # 4. APLICACIÓN DEL TEOREMA DE BAYES P(H|E)
    # ¿Cuál es la probabilidad de que haya un peatón dado que el sensor pitó?
    p_h_given_e = (p_e_given_h * p_h) / p_e
    
    return p_h_given_e, p_e

# --- SIMULACIÓN DE CONDUCCIÓN ---

# Parámetros iniciales
historia_carretera = 0.10  # Solo el 10% de las veces hay obstáculos aquí.
ruido_niebla = 0.20        # La niebla causa falsos positivos el 20% del tiempo.

print("--- INICIANDO PROTOCOLO DE INCERTIDUMBRE ---")
print("[Situación]: Conducción nocturna con visibilidad reducida.")
print("[Sensor]: ¡ALERTA DE OBSTÁCULO DETECTADA!")

# La IA ejecuta la inferencia
prob_real, prob_alerta = sistema_decision_bayesian(historia_carretera, ruido_niebla)

# --- PANEL DE CONTROL DE LA IA ---
print("\n" + "="*55)
print(" DIAGNÓSTICO DE RIESGO BAYESIANO ")
print("="*55)
print(f"Confianza previa en la zona:    {historia_carretera*100:.1f}% de riesgo")
print(f"Probabilidad de aviso de radar: {prob_alerta*100:.1f}%")

print(f"\nRESULTADO: Probabilidad real de peatón: {prob_real*100:.1f}%")

# Toma de decisión crítica
if prob_real > 0.50:
    print("\n[DECISIÓN]: RIESGO CRÍTICO -> Ejecutando Frenado Automático.")
else:
    print("\n[DECISIÓN]: POSIBLE FALSO POSITIVO -> Reducir velocidad por precaución.")
    