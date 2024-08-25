#Tenemos un motor que en cada vuelta, recorre 150 metros
#El motor, va a parar a las 10 vueltas
#en cada vuelta, debe mostrarse la distancia recorrida

vueltas = 0
distancia = 0
while vueltas<10:
    distancia+=150
    vueltas+=1
    print('Distancia: '+str(distancia))

print('Termino de andar')

