dic = {
    'nombre' : "lucas",
    "apellido" : "Dalto",
    "sub" : 100000
}
#recorriendo un diccionario para obtener la clave
for key in dic:
    print(f'la clave es: {key}')

#recorriendo un diccionario con iterms() para obtener la clave y el valor   
for datos in dic.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es {key} y el valor es {value}')