#1.	Leer una matriz B de orden M*A y un número K. Multiplicar todos los elementos de la matriz por el número K. Mostrar la matriz resultante.

import random

M = int(input("Dame la cantidad de filas de la matriz: "))
A = int(input("Dame la cantidad de columnas de la matriz: "))
K = int(input("Dame un numero para multiplicar la matriz: "))

B = [[random.randint(1, 100) for _ in range(A)] for _ in range(M)]

for fila in B:
    print(fila)

for i in range(M):
    for j in range(A):
        B[i][j] *= K

print("Matriz resultante: ")
for fila in B:
    print(fila)


