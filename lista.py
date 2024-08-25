marcas = ['ford','chevrolet','fiat']
print(marcas[1])
marcas[2] = 'ferrari'
print(marcas[2])
indice =2
print(marcas[indice])

for i in range(0, len(marcas)):
    print(marcas[i])

mi_lista = ['pepe',24, 1.65, False, [1,2,3]]

for i in range(len(mi_lista)):
    print(mi_lista[i])

print(mi_lista)

mi_otra_lista = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(mi_otra_lista)):
    for j in range(len(mi_otra_lista[i])):
        print(mi_otra_lista[i][j])

print(mi_otra_lista[1][1])

v1 = mi_otra_lista[1]
print(v1[1])
mi_tercer_lista = [[1,2,3],[1,[10,11,12],1]]

print(mi_tercer_lista[1][1][2])
mi_tercer_lista[1][1][2] = 459803
print(mi_tercer_lista)