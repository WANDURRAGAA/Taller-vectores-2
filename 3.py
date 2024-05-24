# 3.Hacer un algoritmo que llene una matriz de 10*10 y determine la posición [renglón,columna] del número mayor almacenado en la matriz. Los números son diferentes.

import random
a = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

numero_maximo = 0
posicion_maxima = (0, 0)

for i in range(10):
    for j in range(10):
        if a[i][j] > numero_maximo:
            numero_maximo = a[i][j]
            posicion_maxima = (i, j)

for fila in a:
    print(fila)

print(f"La posicion del numero max {numero_maximo} es: {posicion_maxima}")
