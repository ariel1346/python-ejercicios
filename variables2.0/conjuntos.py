conjunto = set(["dato 1"])

#metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset (["dato1","dato2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)


#teoria de conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) 
resultado = conjunto2 <= conjunto1

#verificasndo si es un cubconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1


#verificar  si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)