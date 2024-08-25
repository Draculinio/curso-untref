#Hay una concesionaria de autos
#Se venden 3 tipos de auto
#Ford, Chevrolet, Fiat
#Los autos ford valen 15000 dolares
#Los autos chevrolet valen 14000 dolares
#Los autos Fiat valen 11000 dolares
#Los autos vienen en color blanco, rojo o negro
#SI el color que quiere el cliente es distinto, se le agregan 1500 dolares
#Tambien pueden ser autos usados. Por cada a;o hacia atras, se descuentan 550 dolares.
#El menor valor va a ser 1000 dolares
#Van a venir n clientes a la concesionaria
#A cada cliente se le va a pedir: auto, color, a;o
#Se debe informar todos estos datos mas el valor final del auto
#en caso de que por cualquier motivo no se pueda vender el auto. Debe informarse en 
#lugar del valor, que no se puede concretar la venta.

def elegir_marca():
    ford = 15000
    chevrolet = 14000
    fiat = 11000
    #Primero pregunto por la marca
    precio = 0
    correcto = False
    while correcto == False:
        correcto = True
        marca = input('Ingrese marca de auto: ')
        if marca == 'ford':
            precio =ford
        elif marca == 'chevrolet':
            precio =chevrolet
        elif marca == 'fiat':
            precio =fiat
        else:
            print('La marca no existe')   
            correcto = False
    return precio

def elegir_color():
    p_color = 0
    color = input('Ingrese color:')
    if color != 'blanco' and color!='rojo' and color!='negro':
        p_color = 1500
    return p_color

def fabricacion():
    a_fab = int('Ingrese a;o de fabricacion: ')
    antiguedad = 2024 - a_fab
    return antiguedad*550



otro_cliente = 'y'
while otro_cliente == 'y':
    precio = elegir_marca()
    #Segundo pregunto por el color
    precio += elegir_color()
    #tercero pregunto a;o de fabricacion
    precio -= fabricacion()
    if precio < 1000:
        precio = 1000
    print('Precio final: '+str(precio))
    otro_cliente = input('Hay otro cliente?')