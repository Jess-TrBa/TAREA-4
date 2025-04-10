#Eres un profesor vengativo y una de tus manías es que los estudiantes se apresuren
#en sus exámenes. Para darles una lección, decides dar ceros a los tres primeros estudiantes que
#saquen menos de 60 puntos, en el orden que entregaron sus exámenes.
#Dada un arreglo 1-D de números enteros, identifica los tres primeros valores menores a 60 y
#reemplázalos por cero.

import numpy as np

def reemplazar_tres_primeros_menores_a_60(calificaciones):
    contador = 0 
    
    for i in range(len(calificaciones)):
        if calificaciones[i] < 60 and contador < 3:
            calificaciones[i] = 0
            contador += 1
    
    return calificaciones

generator = np.random.default_rng (1010)
calificaciones = np.round(generator.uniform (low = 1, high = 100, size = 25))
print(f"Las calificaciones obtenidas son las siguientes: {calificaciones}")

resultado = reemplazar_tres_primeros_menores_a_60(calificaciones)
print(f"Las calificaciones reemplazadas con los valores 0 en los primeros tres que sacaron calif < 60 son {resultado}")

indices_ceros = np.where(resultado == 0)[0]  

print("Índices de las calificaciones de ceros:", indices_ceros)