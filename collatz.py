#Si el numero es impar nro*3 +1
#Si es par nro/2

nro = int(input('Ingrese Numero: '))

while nro > 1:
    if nro%2 == 0:
        nro = int(nro/2)
    else:
        nro = (nro*3)+1
    print(nro)
