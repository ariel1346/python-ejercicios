#importando un modulo y asignadole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos 2 funciones 
from modulo_saludar import saludar,saludar_raro

#creamos las variables con los saludos
saludo = saludar('lucas')
saludo2 = saludar_raro('pedro')

#mostramos los resultados
print(saludo)
print(saludo2)


#para ver las propiedades y metodos de el namespace
#print(dir(namespace))


#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)