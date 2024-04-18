import pandas as pd

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv('archivos\\datos.csv')
df2 = pd.read_csv('archivos\\datos.csv')

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el detaframe por la edad
df_orden_ascendente = df.sort_values("edad")


#ordenandolo de forma descendente
df_orden_desendente = df.sort_values("edad",ascending=False)


#concatenando los 2 dataframe
df_concatenado = pd.concat([df,df2])


#accediendo a las primeras fila con head()
primeras_filas = df.head(3)

#accediendo a las ultimas fila con tail()
ultimas_filas = df.tail(3)


#accediendo a la cantidad de filas y columnas con shape()
#filas_y_columans_totales = df.shape

#desempaquetando
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()



#accediendo a la edad de la fila 2  con loc
elemento_especifico_loc = df.loc [2,'edad']
#print(elemento_especifico_loc)

#accediendo a la edad de la fila 2 conm iloc (iloc es por indice)
elemento_especifico_loc = df.iloc [2,2]


#accediendo a todos las filas de una columna con loc
apellidos_loc = df.loc[:'apellido']

#accediendo a todos las filas de una columna con iloc
apellidos = df.iloc[:,1]



#accediendo a la fila 3 con loc
fila3 = df.loc[2,:]


#accediendo a filas con edad mayor que 30
#1er dato es fila, 2do es columna
mayor_que_30 = df.loc[df['edad']>30,:]
print(mayor_que_30)

