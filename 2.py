# 2.	Lea dos matrices N * M y a continuación:

# a)	Genere una tercera con la suma de ambas
# b)	Genere una cuarta con la multiplicación de ambas, si es posible
# Muestre las matrices resultantes

import random

N = int(input("Dame la cantidad de filas de la matriz: "))
M = int(input("Dame la cantidad de columnas de la matriz: "))

matriz1 = [[random.randint(1, 100) for _ in range(M)] for _ in range(N)]
matriz2 = [[random.randint(1, 100) for _ in range(M)] for _ in range(N)]

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila)

matriz3 = [[matriz1[i][j] + matriz2[i][j] for j in range(M)] for i in range(N)]
matriz4 = [[matriz1[i][j] * matriz2[i][j] for j in range(M)] for i in range(N)]

print("Suma:")
for fila in matriz3:
    print(fila)

print("Multiplicación:")
for fila in matriz4:
    print(fila)