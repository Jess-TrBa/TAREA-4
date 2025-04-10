#Eres un profesor vengativo y una de tus manías es que los estudiantes se apresuren
#en sus exámenes. Para darles una lección, decides dar ceros a los tres primeros estudiantes que
#saquen menos de 60 puntos, en el orden que entregaron sus exámenes.
#Dada un arreglo 1-D de números enteros, identifica los tres primeros valores menores a 60 y
#reemplázalos por cero.

import numpy as np

def reemplazar_tres_primeros_menores_a_60(calificaciones):
    contador = 0 #generamos un contador donde iremos agregando las calificaciones menores a 60
    
    for i in range(len(calificaciones)):
        if calificaciones[i] < 60 and contador < 3: #buscamos las 3 primeras calificaciones menores a 60
            calificaciones[i] = 0 #y las sustituimos por 0
            contador += 1
    
    return calificaciones

# snippet de código para generar datos:
generator = np.random.default_rng (1010)
calificaciones = np.round(generator.uniform (low = 1, high = 100, size = 25))
print(f"Las calificaciones obtenidas son las siguientes: {calificaciones}")

resultado = reemplazar_tres_primeros_menores_a_60(calificaciones)
print(f"Las calificaciones reemplazadas con los valores 0 en los primeros tres que sacaron calif < 60 son {resultado}")
#adicionalmente para buscar a los alumnos que sacaron dicha calificacion usaremos los indices:
indices_ceros = np.where(resultado == 0)[0]  

print("Índices de las calificaciones de ceros:", indices_ceros)