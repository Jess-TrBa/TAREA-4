#10 peces ocupan un arreglo 3-D de 5x5x5 de agua. Cada pez decide moverse a la
#posición (i, j, k) dado por el arreglo 2-D que esta más adelante. Si múltiples peces terminan
#ocupando la misma celda, el pez de mayor tamaño se come al más pequeño. Determina que peces
#sobreviven.

import numpy as np

locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

generator = np.random.default_rng(1010)
weights = generator.normal(size=10)
print(f"Los pesos son: {weights}")

#generamos un diccionario para el tanque
tanque = {}

# Movemos cada pez a su nueva posición y registramos su peso
for pez in range(len(locs)):
    position = tuple(locs[pez])  # Lo convertimos a tupla para usar como clave en el diccionario de tanque
    if position in tanque:
        # Si ya hay un pez en esta celda, comparamos los pesos:
        if weights[pez] > tanque[position][1]:
            # Si el nuevo pez es más grande, reemplazamos al existente ya que se lo come
            tanque[position] = (pez, weights[pez])
    else:
        # Si no hay pez en esta celda, agregamos entonces a este nuevo pez:
        tanque[position] = (pez, weights[pez])

# Obtener los numeros de los peces que sobrevivieron:
sobrevivientes = [pez[0] for pez in tanque.values()]
sobrevivientes.sort()  # Ordenar los numeros para visualizarlo mejor

print("Peces que sobreviven:", sobrevivientes)