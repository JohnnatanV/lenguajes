def suma(a, b):
    print(a + b)


# suma(2, 5)


def sumax(*numeros):
    resultado = 0

    for numero in numeros:
        resultado += numero
    print(resultado)


sumax(3)
sumax(2, 3)
sumax(2, 4, 5)
