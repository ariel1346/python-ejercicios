#2 listas, una con nombres y otra con apellidos
nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto",'Zing','Dalto','Robetix','Tarado']

# registrar esta informacion en un TXT de forma optima 

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as archi:
    archi.writelines("Los datos son \n \n")
    [archi.writelines(f'\nNombre: {n}\nApellido: {a}\n---------------')for n,a in zip(nombres,apellidos)]
    
# lo mismo que arriba pero escrito en 2 lineas de copdigo

#for n,a in zip(nombres,apellidos):
    #archi.writelines(f'\nNombres: {n}\nApellidos: {a}\n-----------------')    