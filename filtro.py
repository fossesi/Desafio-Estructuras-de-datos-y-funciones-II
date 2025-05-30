import sys


precios = {'Notebook': 700000,
          'Teclado': 25000,
          'Mouse': 12000,
          'Monitor': 250000,
          'Escritorio': 135000,
          'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral):
 filtro = {k for k,v in diccionario.items() if v > umbral}
 return list(filtro)

filtrados = filtrar(precios, 30000)
print("Los productos mayores al umbral son: ",", ".join(filtrados))