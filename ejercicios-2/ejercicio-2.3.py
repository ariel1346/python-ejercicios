def fibonacci(numero):
    a,b = 0,1
    fibonacci_lista = []
    for e in range(numero):
        if a+b > numero: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b
    return fibonacci_lista
resultado = fibonacci(20)

print(resultado)