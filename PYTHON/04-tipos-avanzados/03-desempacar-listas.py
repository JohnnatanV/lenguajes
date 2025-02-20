numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# FEO!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]


# primero, segundo, tercero = numeros

primero, segundo, *otros, penul, ultimo = numeros

# print(tercero, segundo, primero)  # 3 2 1

print(primero, segundo, otros, penul, ultimo)
