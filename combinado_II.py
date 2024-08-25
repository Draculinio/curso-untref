# Ingresamos n edades
# guardamos todas las edades mayores a 30
# mostramos por pantalla las edades mayores a 30
# mostrar edades al final
# Si la edad es menor o igual a 30, mostrar cuantos a;os faltan para los 30
cantidad  =int(input('Ingrese cantidad de edades: '))
edades = ''
for i in range(cantidad):
    edad = int(input('Ingrese edad: '))
    if edad > 30:
        edades = edades + str(edad) +' '
    else:
        print('Para grabar su edad le faltan '+str(31 - edad)+ ' a;os')
print(edades)