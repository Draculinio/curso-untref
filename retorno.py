import random

def paridad(nro):
    return nro%2 == 0

#funcion dado 
def dado(caras, cantidad):
    #resultado = random.randint(1,caras)*cantidad
    return random.randint(1,caras)*cantidad

calcular_numero = paridad(45)
print(calcular_numero)

resultado_dado = dado(8,2)
print(resultado_dado)