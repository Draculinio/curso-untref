edad = int(input('Ingrese edad: '))

mensaje = ''
if edad<18:
    mensaje = 'Es menor'
elif edad >=60:
    mensaje = 'Es jubilado'
else:
    mensaje = 'Es mayor'

print(mensaje)