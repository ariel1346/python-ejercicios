#usando open para abrir un archivo con una codificacion universal (UFT-8)
archivo = open("archivos\\texto_de_dalto.txt", encoding="UTF-8")

#leer archivo completo
archivo = archivo.read()

#leer una sola linea
#lineas = archivo.readline()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#cerrar archivo
archivo.close()

print(archivo)
