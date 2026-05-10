#¿Qué es la Regla de la Cadena?
# La Regla de la Cadena permite calcular la probabilidad de una intersección de múltiples eventos 
# (que ocurra A, luego B, luego C...). Su poder reside en que no requiere que los eventos sean 
# independientes; de hecho, está diseñada para manejar la dependencia.La fórmula general para tres 
# eventos es:$$P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)$$

# En términos simples: la probabilidad de que toda la secuencia ocurra es igual a la probabilidad 
# del primer evento, multiplicada por la probabilidad del segundo dado que el primero ya pasó, y 
# así sucesivamente.

# --- MOTOR DE PROBABILIDAD SECUENCIAL ---

def simular_regla_cadena(inventario_inicial, ruta_secuencia):
    """
    Calcula P(E1 ∩ E2 ∩ ... ∩ En) actualizando el estado del sistema en cada paso.
    """
    estado_actual = inventario_inicial.copy()
    prob_acumulada = 1.0
    bitacora = []

    print(f"--- INICIO DE LA CADENA DE EVENTOS ---")
    
    for i, evento in enumerate(ruta_secuencia):
        total_disponible = sum(estado_actual.values())
        
        # 1. Verificación de existencia (Evitar división por cero o eventos imposibles)
        if total_disponible == 0 or estado_actual.get(evento, 0) <= 0:
            print(f"  [!] La secuencia se rompió en el paso {i+1}: '{evento}' ya no está disponible.")
            return 0.0
        
        # 2. Cálculo de la Probabilidad Condicional P(Evento_i | Anteriores)
        prob_paso = estado_actual[evento] / total_disponible
        
        # 3. Actualización de la probabilidad conjunta (Regla de la Cadena)
        prob_acumulada *= prob_paso
        
        print(f"  Paso {i+1}: Sacar {evento.ljust(6)} | P = {estado_actual[evento]}/{total_disponible} = {prob_paso:.4f}")
        
        # 4. EFECTO SECUNDARIO: Modificamos el entorno (Sin reemplazo)
        # Al ocurrir el evento, hay una unidad menos de ese recurso para el futuro.
        estado_actual[evento] -= 1

    return prob_acumulada

# --- ESCENARIO: Extracción de muestras de un servidor ---
# Tenemos un servidor con 10 archivos: 5 de Texto, 3 de Imagen y 2 de Video.
servidor = {
    'Texto': 5,
    'Imagen': 3,
    'Video': 2
}

# Queremos saber la probabilidad de extraer: Imagen -> Texto -> Imagen
objetivo = ['Imagen', 'Texto', 'Imagen']

# Ejecución
prob_total = simular_regla_cadena(servidor, objetivo)

print("\n" + "="*50)
print(f" RESULTADO: P({', '.join(objetivo)}) ")
print("="*50)
print(f"La probabilidad de esta secuencia exacta es: {prob_total:.5f}")
print(f"Representa un {prob_total*100:.2f}% de probabilidad en un universo sin reemplazo.")
