#falto el profe y los pibes van armar la clase.

#pedir el nombre y la edad de los companeros que vinieron a clase.

#funcion para obtener al asistente y al profesor segun la edad
def obtener_pibes(cantidad_de_pibes):
    
    #creando la lista con los pibes
    pibes = []
    
    #ejecutanto un for para pedir informacion de cada pibe
    for i in range(cantidad_de_pibes):
        nombre = input('ingrese el nombre del pibe: ')
        edad = int(input('ingrese la edad del pibe'))
        pibe = (nombre,edad)
        
        #agregando la informacion a la lista
        pibes.append(pibe)
        
    #ordenandolos de menor a mayor segun la edad    
    pibes.sort(key=lambda x:x[1])
    
    #pibes[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = pibes[0][0]
    profesor = pibes[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorno al funcion
asistente,profesor = obtener_pibes(5)

#mostramos el resultado
print(f'El profesor es :{profesor} y el asistente es {asistente}')