# 5.Hacer un algoritmo que llene una matriz de 5 * 5 y que almacene la diagonal principal en un vector. Imprimir el vector resultante.

import random

mionca = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        mionca[i][j] = random.randint(1, 10)

diagonal_principal = [mionca[i][i] for i in range(5)]

print("Matriz:")
for renglon in mionca:
    print(renglon)
print("Diagonal principal:", diagonal_principal)