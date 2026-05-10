#¿Qué es el Muestreo por Rechazo?
# Imagina que quieres recortar una galleta con una forma muy extraña (una curva de probabilidad 
# compleja $P(x)$). 

# Como no tienes un molde exacto, usas un método ingenioso:
# Muestreo Directo: Colocas una lámina de masa rectangular que cubra todo el espacio (una distribución 
# simple $Q(x)$, como una caja uniforme).
# Lanzamiento de Dardos: Lanzas dardos al azar sobre toda la lámina.
# El Filtro (Rechazo): Si el dardo cae dentro de la zona de tu "galleta", te quedas con ese punto 
# (Aceptado). 
# Si cae fuera, en la masa que sobra, lo descartas (Rechazado).Al final, los puntos aceptados 
# tendrán exactamente la forma de la curva compleja que querías imitar.

import random
import math

# --- 1. EL MUNDO REAL: Curva de Actividad del Servidor ---
def curva_actividad_real(hora):
    """
    Representa la probabilidad P(x) de que un usuario entre al sitio.
    Picos: Mañana (trabajo) y Noche (ocio).
    """
    if not (0 <= hora <= 24): return 0.0
    
    # Simulación de picos usando funciones gaussianas (campanas)
    pico_dia = 0.6 * math.exp(-0.1 * (hora - 10)**2)
    pico_noche = 0.8 * math.exp(-0.1 * (hora - 20)**2)
    base_ruido = 0.1
    
    return min(pico_dia + pico_noche + base_ruido, 1.0)

# --- 2. EL MOTOR DE MUESTREO ---
def generar_usuario_sintetico():
    """
    Algoritmo de Rejection Sampling para 'esculpir' la curva real.
    """
    intentos_locales = 0
    M = 1.0  # Altura máxima de nuestra "caja" de búsqueda
    
    while True:
        intentos_locales += 1
        
        # PASO A: Proponer una hora al azar (Muestreo Directo / Uniforme)
        hora_propuesta = random.uniform(0, 24)
        
        # PASO B: El dardo de validación
        u = random.uniform(0, M)
        
        # PASO C: ¿El dardo está bajo la curva de actividad?
        if u <= curva_actividad_real(hora_propuesta):
            return hora_propuesta, intentos_locales

# --- 3. EJECUCIÓN DE LA SIMULACIÓN ---
total_usuarios = 5000
log_usuarios = []
gran_total_intentos = 0

print(f"[*] Generando {total_usuarios} perfiles de conexión...")

for _ in range(total_usuarios):
    hora, costo = generar_usuario_sintetico()
    log_usuarios.append(hora)
    gran_total_intentos += costo

# --- 4. ANALÍTICA DE LA IA ---
print("\n" + "="*40)
print("   REPORTE DE GENERACIÓN SINTÉTICA")
print("="*40)

eficiencia = (total_usuarios / gran_total_intentos) * 100

print(f"Usuarios creados:     {total_usuarios}")
print(f"Costo computacional:  {gran_total_intentos} intentos")
print(f"Eficiencia del molde: {eficiencia:.2f}%")

# Visualización rápida de la distribución generada (Histograma de texto)
print("\n[Distribución de carga generada]:")
for h in [8, 10, 12, 16, 20, 23]:
    count = len([x for x in log_usuarios if h <= x < h+1])
    print(f" {h:02d}:00 | {'█' * (count // 20)} ({count} users)")
    