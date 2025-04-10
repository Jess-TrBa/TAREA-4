#Tu eres un científico de las relaciones, y has desarrollado un cuestionario 
# que determina el puntaje de amor, es decir, un valor real entre cero y cien.
# Tu teoría es que dos personas con puntajes de amor similares deberían de hacer 
# un buen match. Dado los puntajes del amor para 10 personas distintas, crea 
# un arreglo 2-D donde cada entrada (i, j) da la diferencia absoluta entre los 
# puntajes del amor de la persona i y la persona j.


import numpy as np
generator = np.random.default_rng (1010)
data = np.round(generator.uniform (low = 1, high = 100, size = 10))
print(data)
matriz_diferencias = np.abs(data[:, np.newaxis] - data) #aquí se genera una matriz donde cada valor de la línea 
#superior se va restando a cada valor de la columna inicial. Esto lo hace por broadcasting. Se utiliza np.abs para sacar el valor absoluto
print("Matriz de diferencias absolutas:")
print(matriz_diferencias)

diferencias_persona_0 = matriz_diferencias[0, :] 
arr_sin_ceros0 = np.where(diferencias_persona_0 == 0, np.inf, diferencias_persona_0)
indice_menor0 = np.argmin(arr_sin_ceros0)
mejor_match_persona0 = indice_menor0
print(f"El mejor match para la persona 0 es la persona {mejor_match_persona0}")

diferencias_persona_1 = matriz_diferencias[1, :] 
arr_sin_ceros1 = np.where(diferencias_persona_1 == 0, np.inf, diferencias_persona_1)
indice_menor1 = np.argmin(arr_sin_ceros1)
mejor_match_persona1 = indice_menor1
print(f"El mejor match para la persona 1 es la persona {mejor_match_persona1}")

diferencias_persona_2 = matriz_diferencias[2, :] 
arr_sin_ceros2 = np.where(diferencias_persona_2 == 0, np.inf, diferencias_persona_2)
indice_menor2 = np.argmin(arr_sin_ceros2)
mejor_match_persona2 = indice_menor2
print(f"El mejor match para la persona 2 es la persona {mejor_match_persona2}")

diferencias_persona_3 = matriz_diferencias[3, :] 
arr_sin_ceros3 = np.where(diferencias_persona_3 == 0, np.inf, diferencias_persona_3)
indice_menor3 = np.argmin(arr_sin_ceros3)
mejor_match_persona3 = indice_menor3
print(f"El mejor match para la persona 3 es la persona {mejor_match_persona3}")

diferencias_persona_4 = matriz_diferencias[4, :] 
arr_sin_ceros4 = np.where(diferencias_persona_4 == 0, np.inf, diferencias_persona_4)
indice_menor4 = np.argmin(arr_sin_ceros4)
mejor_match_persona4 = indice_menor4
print(f"El mejor match para la persona 4 es la persona {mejor_match_persona4}")

diferencias_persona_5 = matriz_diferencias[5, :] 
arr_sin_ceros5 = np.where(diferencias_persona_5 == 0, np.inf, diferencias_persona_5)
indice_menor5 = np.argmin(arr_sin_ceros5)
mejor_match_persona5 = indice_menor5
print(f"El mejor match para la persona 5 es la persona {mejor_match_persona5}")

diferencias_persona_6 = matriz_diferencias[6, :] 
arr_sin_ceros6 = np.where(diferencias_persona_6 == 0, np.inf, diferencias_persona_6)
indice_menor6 = np.argmin(arr_sin_ceros6)
mejor_match_persona6 = indice_menor6
print(f"El mejor match para la persona 6 es la persona {mejor_match_persona6}")

diferencias_persona_7 = matriz_diferencias[7, :] 
arr_sin_ceros7 = np.where(diferencias_persona_7 == 0, np.inf, diferencias_persona_7)
indice_menor7 = np.argmin(arr_sin_ceros7)
mejor_match_persona7 = indice_menor7
print(f"El mejor match para la persona 7 es la persona {mejor_match_persona7}")

diferencias_persona_8 = matriz_diferencias[8, :] 
arr_sin_ceros8 = np.where(diferencias_persona_8 == 0, np.inf, diferencias_persona_8)
indice_menor8 = np.argmin(arr_sin_ceros8)
mejor_match_persona8 = indice_menor8
print(f"El mejor match para la persona 8 es la persona {mejor_match_persona8}")

diferencias_persona_9 = matriz_diferencias[9, :] 
arr_sin_ceros9 = np.where(diferencias_persona_9 == 0, np.inf, diferencias_persona_9)
indice_menor9 = np.argmin(arr_sin_ceros9)
mejor_match_persona9 = indice_menor9
print(f"El mejor match para la persona 9 es la persona {mejor_match_persona9}")