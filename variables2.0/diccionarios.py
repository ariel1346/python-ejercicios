#creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido = "dalto")

#las listas no pueden ser claves y usamos frozenset para meter ocnjuntos si
diccionario = {frozenset(["dalto","rancio"]):"jaajja"}

#creamos diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creamos diccionarios con fromkeys() cambiando el valor por defecto: a "no se "
diccionario = dict.fromkeys(["nombre","apellido"], "no se")

print(diccionario)

