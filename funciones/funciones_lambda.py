
numeros = [1,2,3,4,5,6,7,8,9,14,12,20]

#creando una function lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2


#creando funcion comun que diga si es par o no 
# def es_par(numeros):
#       if(numeros%2 ==1):
#         return True


#usando filter con una function comun
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda

numeros_pares = filter(lambda hola:hola%2 == 0,numeros)
print(list(numeros_pares))