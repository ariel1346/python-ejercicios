diccionario = {
    "nombre" : 'lucas',
    "apellido": 'dalto',
    "sub" : 1000000
} 

#nos devuelve un objeto dict_item que se puede iternar dict_item

claves = diccionario.keys()

#obteniendo un elemento con get() si no encuentra nada el programa continua 
valor_de_kasds= diccionario.get("kasds")
print("hola papa, el progrma continua")

#elimina todo del diccionario
#diccionario.clear()

#eliminando un elemento deldiccionario
diccionario.pop('sub', 'nombre')


#obteniedo un elemento del diccionario iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)