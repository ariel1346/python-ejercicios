#forma no optima de sumar valores
# def suma(a,b):
#     return a+b

# resultado = suma(5,8)
# print(resultado)

# def suma(lista):
#     numeros_sumados = 0
#     for numeros in lista:
#         numeros_sumados = numeros_sumados + numeros
#     return numeros_sumados
    
# resultado = suma([5,6,2,6,2])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,6,2,6,2])
print(resultado2)


#lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma(apellido,nombre,*numeros):
    return f'{nombre} {apellido} la suma de tus numeros es: {sum(numeros)}'

resultado = suma('perez','jorge',5,6,2,6,2)
