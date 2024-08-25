veces = int(input('Cuantas veces lo hacemos:'))

for i in range(0,veces):
    edad = int(input('Ingrese edad: '))
    mensaje = ''
    if edad<18:
        mensaje = 'Es menor'
    elif edad >=60:
        mensaje = 'Es jubilado'
    else:
        mensaje = 'Es mayor'

    print(mensaje)