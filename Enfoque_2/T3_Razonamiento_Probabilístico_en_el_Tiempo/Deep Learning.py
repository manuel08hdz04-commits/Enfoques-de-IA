'''
Deep Learning simple
Red neuronal básica
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# ====================== DATOS ========================================

# [horas_estudio, tareas]
X = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [3, 2],
    [4, 3],
    [5, 4]
])

# Resultado:
# 0 = reprueba
# 1 = aprueba
y = np.array([0, 0, 0, 1, 1, 1])

# ====================== MODELO =======================================

modelo = Sequential()

# Capa oculta
modelo.add(Dense(
    4,
    input_dim=2,
    activation='relu'
))

# Capa de salida
modelo.add(Dense(
    1,
    activation='sigmoid'
))

# ====================== COMPILAR =====================================

modelo.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# ====================== ENTRENAMIENTO ================================

modelo.fit(
    X,
    y,
    epochs=200,
    verbose=0
)

# ====================== PREDICCIÓN ===================================

nuevo = np.array([[4, 2]])

prediccion = modelo.predict(nuevo)

print("\nDeep Learning:\n")

print("Probabilidad de aprobar:")
print(round(prediccion[0][0], 3))