def maior_numero(a, b, c):
    #Compara qual numero é maior...
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


resultado = maior_numero(10, 25, 18)
print(resultado)