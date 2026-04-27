'''
VALOR DE LA INFORMACIÓN

Calcula el valor esperado de una decisión
usando probabilidades.
'''

def valor_esperado(prob, util):
    return sum(prob[e] * util[e] for e in prob)

# EJEMPLO (clima)
prob = {"lluvia":0.3,"sol":0.7}
util = {"lluvia":10,"sol":100}

print("\nValor esperado del clima:")
print(valor_esperado(prob, util))
