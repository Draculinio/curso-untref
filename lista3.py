a = 1
b = a
a = 2
print(a)
print(b)

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
lista_dos = lista.copy()
print(lista_dos)
lista[3] = 5
print(lista)
print(lista_dos)

#lista n n n n n n n n n
#lista_dos apuntar a esas mismas direcciones de memoria

lista_dos.insert(4,1000)
print(lista_dos)

lista_tres = [1000,500,100,10000,10000000,3432,500]
lista_tres.sort()
print(lista_tres)
lista_tres.remove(500)
print(lista_tres)
print(min(lista_tres))
print(max(lista_tres))