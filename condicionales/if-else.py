ingreso_mensual = 72000
gasto_mensual = 80000


#if anidados y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas bien')
    else:
        print('y pa estas gastando una banda hay que ver si te alcanza')

elif ingreso_mensual > 1000 :
    print('estas bien en latinoamertica')  
    
elif ingreso_mensual > 500:
    print('estas bien en argentina')
    
    
elif ingreso_mensual > 200 :
    print('esta bien en venezuela') 
    
else: 
    print('sos pobre')               