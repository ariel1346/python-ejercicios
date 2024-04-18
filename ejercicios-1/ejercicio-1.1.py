
#promedio de duracion del curso de python
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5 
crudo_dalto = 3.5



#diferencia de duracion
diferencia_con_min = round( 100 - dalto_curso / otros_cursos_min)
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido 
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


#mostrando las dif. de duracion ejercicio A
print("---------------------------")
print("el curso de dalto dura")
print(f'- un {diferencia_con_min}% menos que el mas rapido')
print(f'- un {diferencia_con_max}% menos que el mas lento')
print(f'- un {diferencia_con_promedio}% menos que el promedio')
print("--------------------------")
#mostrando la cantidad de espacios vacios que se remueven ejrcicio b
print(f'un curso promedio elimino un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print('--------------------------')
#mostrando diferencias si los cursos duraran 10 horas ejercicio C
print(f'ver 10 horas de este curso equivale a ver { 100 * otros_cursos_promedio // dalto_curso / 10 } horas de otros cursos')
print(f'ver 10 horas de este curso equivale a ver { 100 * dalto_curso // otros_cursos_promedio / 10 } horas de este cursos')
print("---------------------------")