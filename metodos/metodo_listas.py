#creando una lista con list() 
lista = list([34,65,44,True])

resultado = len(lista)

#agregando un  elemento a la lista
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(1,'toma mamama')

#agregando varios elementos a la lista
lista.extend([2030])

#eliminandoun elemento de la lista por su indice
lista.pop(3)

#removiendo un elemento de la lista por su valor
lista.remove('toma mamama')

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reverse)
lista.sort(reverse=True)

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista 
#debe ser igual al elemento de la lista 
elemento_encontrado = lista.index(34)


print(dir(set(['gkdflsgd','fdiksfj'])))
