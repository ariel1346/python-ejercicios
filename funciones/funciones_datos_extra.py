#creando uan funtion de 3 parametros
# def frase(nombre,apellido,adjetivo):
#     return f'hola {nombre} {apellido} sos muy {adjetivo}'

# #utilizando keywords arguments
# frase_resultado = frase(adjetivo = 'inteligente',nombre = 'lucas',apellido = 'dalto')
# print(frase_resultado)


#creando la misma funtion con um parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = 'tonto'): #valor opcional, valor por defecto y definiendo tonto
    return f'hola {nombre} {apellido} sos muy {adjetivo}'

frase_resultante = frase('lucas','dalto')
print(frase_resultante)