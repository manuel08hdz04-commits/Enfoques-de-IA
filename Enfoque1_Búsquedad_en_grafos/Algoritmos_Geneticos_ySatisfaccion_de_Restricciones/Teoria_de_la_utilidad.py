
def funcion_utilidad(estado):
    return estado["dinero"] - 2 * estado["riesgo"]

estado = {"dinero": 120, "riesgo": 40}
print("Utilidad:", funcion_utilidad(estado))
