with open('archivos\\texto_de_dalto.txt','a') as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write('\n')
    for i in range(5):
        #agregando lineas
        archivo.write(f' Linea {i+1} agregando\n')