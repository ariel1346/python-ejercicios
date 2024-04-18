animales = ['gato','perro','loro','cocodrilo']
numeros = [52,16,14,72]

# #recorrienod la lista animales
# for animal in animales:
#     print(f'Ahora la variable animal es igual: {animal}')
    
# #recorriendo la lista numeros y multiplicando cada valor por 10 
# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)
    
#iterando 2 listas del mismo tamano al mismo tiempo   
# for numero,animal in zip(animales,numeros):
#     print(f'recorriendo la lista 1 : {numero}')
#     print(f'recorrienod la lista 2 : {animal}')
 
#forma no optima de recorrer una lista
for relngfnfg in range(len(animales)) :
    print(animales[relngfnfg])
    
    #forma correcta de recorrer una lista con su indice
# for num in enumerate(numeros) :
#   olor_indice = num[0]
#   pedo_valor = num[1]
#   print(f'el olor_indice es igual {olor_indice}.')
#   print(f'el pedo_valor es igual {pedo_valor}.')
  
#usando el for/else 
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valaor actual {numero}')
else:
    print('el bucle termino')
    
#todo lo anterior funciona exactamente igual para tuplas
