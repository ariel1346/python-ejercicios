cadena1 = 'hola,como,estas,bien'
cadena2 = 'bienvenido a Python '

mayus = cadena1.upper()

minusc = cadena1.lower()

primer_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena  FIND
# si no hay coioncidencias nos devuele -1
busqueda_find = cadena1.find("1")

#buscamos una cadena en otra cadena
busqueda_index = cadena1.index('h')


#si es numerico devolvcemos true sino devolvemos false
es_numerico = cadena1.isnumeric()


#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#buscamos uan cadena en otra cadean, devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count('a')

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")

#verificamos si una cadena termina  con otra cadena dada, si es asi devuelve true
termina_con = cadena1.startswith("an")


# reemplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace("la","como estas ")


#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(type(cadena_separada))