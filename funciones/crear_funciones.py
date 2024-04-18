# #creando una function siplr
# def saludar():   
#     print("hola como estas esta es una funtion")
# #ejecutando la function simple
# saludar()

#creando una function con parametros 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
     adjetivo = 'reina'
    elif (sexo == "hombre"):
     adjetivo = "rey"
    else:
        adjetivo = 'amor'
        
    print(f"hola {nombre} mi {adjetivo}, como estas ?")

saludar("ariel","HOmbre")

#creando una function que nos retorne valores
def crear_contra_ramdon(num):
    chars = "abcdefghi"
    num_entero = str(num) #numero entero lo convertimo a string con str()
    num = int(num_entero[0]) #con int nos devuelve la 1ra posicion ej: 4567 nos quedamos con el 4 
    c1 = num - 2
    c2 = num
    c3 = num - 5
    constrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return constrasena,num
    
#desempaquetando la funtion
password,primer_numero = crear_contra_ramdon(334)


#mostrando los resultados obteniudos y los datos para obtenerlo
print(f'tu password nuevas es:{password}')
print(f'el numero utilizado para crearlas fue:{primer_numero}')