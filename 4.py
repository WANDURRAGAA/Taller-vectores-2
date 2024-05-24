# 4. Hacer un algoritmo que llene una matriz de 7x7. Calcular la suma de cada renglón y almacenarla en un vector, la suma de cada columna y almacenarla en otro vector.

import random
mionca = [[0] * 7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        mionca[i][j] = random.randint(1, 10)

sumas_renglones = []
for renglon in mionca:
    suma_renglon = sum(renglon)
    sumas_renglones.append(suma_renglon)

sumas_columnas = []
for j in range(7):
    suma_columna = sum(mionca[i][j] for i in range(7))
    sumas_columnas.append(suma_columna)

print("Matriz:")
for renglon in mionca:
    print(renglon)
print("Sumas de los renglones:", sumas_renglones)
print("Sumas de las columnas:", sumas_columnas)
