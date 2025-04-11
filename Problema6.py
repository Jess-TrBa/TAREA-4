#Dado un arreglo de 10x10x10 de ceros, establece (i, j, k) = 1 sí, i es impar, j es par y
#k es primo. En otras palabras, establece esos elementos a 1: (1, 0, 2), (1, 0, 3), (1, 0, 5), (1, 0, 7),
#(1, 2, 2)...

import numpy as np

# Generamos una función para verificar si un número es primo:
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: #esto es mas bien par
        return False
    for i in range(3, int(np.sqrt(n)) + 1, 2): #empezamos desde 3 porque 0,1 y 2 ya se analizaron en los pasos anteriores. terminamos 
        #con el valor dado por int(np.sqrt(n)) np.sqrt calcula la raiz cuadrada de n y le agregamos 1., Lo analizamos cada 2 valores.
        if n % i == 0:
            return False
    return True

# Creamos el arreglo 10x10x10 de ceros
arreglo = np.zeros((10, 10, 10), dtype=int)
print(arreglo)

# Definimos los números primos menores que 10
primos = [k for k in range(10) if es_primo(k)]  # [2, 3, 5, 7]
test = ()
# Establecemos 1 en las posiciones que cumplen las condiciones
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i % 2 == 1 and j % 2 == 0 and k in primos: # i % 2 == 1 es impar si el residuo es 1,  j % 2 == 0 es par si el residuo es 0
                test.append((i,j,k))
                arreglo[i, j, k] = 1 #cambiar las posiciones dentro del arreglo de ceros

for t en test:
print(t, t elementos)

# Comprobamos:
print("Posición (1, 0, 2):", arreglo[1, 0, 2]) 
print("Posición (1, 0, 3):", arreglo[1, 0, 3]) 
print("Posición (1, 2, 2):", arreglo[1, 2, 2])  
print("Posición (1, 0, 5):", arreglo[1, 0, 5])
print("Posición (1, 0, 7):", arreglo[1, 0, 7])
print("Posición (1, 0, 5):", arreglo[1, 2, 2])
print("Posición (2, 0, 2):", arreglo[2, 0, 2])  
print("Posición (1, 1, 2):", arreglo[1, 1, 2])  
print("Posición (1, 0, 4):", arreglo[1, 0, 4])  
