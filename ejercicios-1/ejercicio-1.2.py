frase = input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla:")
palabras_separadas = frase.split()   #split nos cuenta los espacios osea la cadena de texto 
cantidad_de_palabras = len(palabras_separadas)

# en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco 
if cantidad_de_palabras > 120:
    print('para flaco no te pedi tanto')
  
  #calculamos cuanto tardaria en decir las palabras y se lo decimos  
print(f'dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'dalto lo diria en {cantidad_de_palabras / 2 } segundos en decirlo')