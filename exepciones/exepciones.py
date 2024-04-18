#creando funcion que suma numeros
def suma_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input('Numero 1:')
        b = input('Numero 2:')
        #intentando convertirlos a entero y sumarlos
        try:
           resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingre los datos
        except:
            print("te pedi un numero gracioso")
        #si todosalio bien terminamos el bucle
        else:
          break
    #mostrando el resultado
    return resultado

print(suma_dos())