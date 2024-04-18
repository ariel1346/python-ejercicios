#creando una funcion que nos devuelva los numeros primos 
#entre 0 y el argumento que pasemos


#crear una funcion que verifique si un numero es primo
def es_primo(numero):
    #verificamos que el numeor pasado(2) no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for e in range(2,numero-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if numero%e== 0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True
    
#creandofuncion que retorna una lista con tods los primos   
def primos_hasta(num):
    #creamos la lista
    primos = []
    for e in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(e)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(e)
    
    #devolvemos la lista
    return primos   
    
#creamos el resultado llamandoa la funcion y lo mostramos   
resultado = primos_hasta(98)
print(resultado)