vehiculo = {'marca':'Ford','modelo':'Fiesta','km':23000}

empleado = {'nombre':'Juan Carlos',
            'direccion':'Pepito 123', 
            'mail':'pepito@gmail.com',
            'sucursales':[12,34,65,18],
            'vehiculo': vehiculo}


print(empleado)
print(empleado['direccion'])
print(empleado['sucursales'])
print(empleado['sucursales'][1])
print(empleado['vehiculo']['marca'])