#¿Qué es la Probabilidad a Priori?
# La probabilidad a priori representa lo que sabemos del mundo antes de observar cualquier evidencia 
# nueva. En el caso de un filtro de spam, si históricamente el 80% de tus correos son basura, 
# tu IA debería tener un "prejuicio" saludable y sospechar de cualquier mensaje nuevo, incluso 
# antes de leer una sola palabra.

# Conceptos clave en Naïve Bayes:
# A Priori ($P(C)$): La frecuencia base de cada clase (Spam vs. Normal) en el historial.
# Verosimilitud ($P(x|C)$): Qué tan probable es encontrar ciertas palabras en los correos que ya 
# sabemos que son Spam.
# Naïve (Ingenuo): Se llama así porque asume que las palabras aparecen de forma independiente 
# entre sí, lo cual no es cierto (ej. "dinero" y "rápido" suelen ir juntas), pero simplifica el 
# cálculo drásticamente y funciona sorprendentemente bien.

# --- CLASIFICADOR DE CORREO POR INFERENCIA A PRIORI ---

# 1. BASE DE CONOCIMIENTO (Dataset de entrenamiento)
historial = [
    ("urgente gana dinero gratis", "Spam"),
    ("oferta exclusiva de dinero", "Spam"),
    ("reunión de equipo lunes", "Normal"),
    ("informe de ventas listo", "Normal"),
    ("invitación a comer pizza", "Normal")
]

def entrenar_filtro(datos):
    """Calcula las probabilidades base (A Priori)."""
    total = len(datos)
    conteos = {"Spam": 0, "Normal": 0}
    vocabulario = {"Spam": [], "Normal": []}

    for texto, etiqueta in datos:
        conteos[etiqueta] += 1
        vocabulario[etiqueta].extend(texto.split())

    # Cálculo A Priori: P(Clase)
    # Si hay 2 correos de Spam entre 5 totales, P(Spam) = 0.4
    a_priori = {k: v / total for k, v in conteos.items()}
    
    return a_priori, vocabulario

# 2. PROCESO DE ENTRENAMIENTO
prob_a_priori, bolsas_palabras = entrenar_filtro(historial)

print(f"--- CREENCIA A PRIORI ---")
print(f"Probabilidad base de Spam:   {prob_a_priori['Spam']*100:.1f}%")
print(f"Probabilidad base de Normal: {prob_a_priori['Normal']*100:.1f}%\n")

# 3. MOTOR DE CLASIFICACIÓN
def calcular_score(mensaje, clase):
    """Calcula el puntaje acumulado: P(Clase) * P(palabra1|Clase) * ..."""
    score = prob_a_priori[clase]
    palabras = mensaje.lower().split()
    
    for p in palabras:
        # Suavizado de Laplace (para no multiplicar por 0 si la palabra es nueva)
        coincidencias = bolsas_palabras[clase].count(p) + 1
        total_palabras_clase = len(bolsas_palabras[clase]) + 100 
        
        # Multiplicamos la creencia previa por la evidencia de la palabra
        score *= (coincidencias / total_palabras_clase)
        
    return score

# 4. PRUEBA DE CAMPO
nuevo_mensaje = "reunión urgente de dinero"
print(f"Analizando: '{nuevo_mensaje}'...")

score_spam = calcular_score(nuevo_mensaje, "Spam")
score_normal = calcular_score(nuevo_mensaje, "Normal")

# Normalización a escala 100% (A Posteriori)
total_score = score_spam + score_normal
prob_final_spam = (score_spam / total_score) * 100

print("\n" + "="*50)
print(" RESULTADO DEL ANÁLISIS PROBABILÍSTICO ")
print("="*50)
print(f"Confianza de que es Spam: {prob_final_spam:.2f}%")

if prob_final_spam > 50:
    print("[Acción]: Bloquear remitente.")
else:
    print("[Acción]: Permitir entrega.")

    