with open('archivos\\texto_de_dalto.txt','w') as archivo:
    #sobreescribiendo el archivo
    #archivo.write('jjajaajajajaj te la recontra lieee')
    
    #agregando 2 lineas con writelines
    archivo.writelines([ '- hola maestro como andas\n','- misericonria toy quebrado\n'])\
    
    #agregando otras 2 lineas
    archivo.writelines([ '- no pero igual me debes\n','- cambiarete lo juro\n'])