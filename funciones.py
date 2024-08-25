#Ver si un numero es par

def es_par():
    nro = int(input('Ingrese numero: '))
    if nro%2 == 0:
        print('Es par')
    else:
        print('Es impar')
    #print('Es par') if int(input('Ingrese numero: '))%2 == 0 else print('Es impar')

es_par()