#creando lista 
fruta = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena= "hola dalto"
numeros = [2,5,8,10]
#evitando que se coma una granada con la sentencia continue
for frut in fruta:
    if frut == "granada":
        continue
    print(f'me voy a comer una: {frut}')
    
#evitar que el bucle siga ejecutandose
for frut in fruta:
    if frut == "pera":
        break
    print(f'me voy a comer una: {frut}')
    
print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena :
    print(letra)
    
    
#for forma de hacerlo
# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)

# print(numeros_duplicados)


#for en una sola linea de codigo duplicamos los numeros
numeros_duplicados =[x*2 for x in numeros]
print (numeros_duplicados)