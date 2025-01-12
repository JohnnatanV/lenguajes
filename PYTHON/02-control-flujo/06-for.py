buscar = 6

# for numero in range(5):
#     print(numero)
#     print(numero*"Hola Mundo ")

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No se encontro el numero buscado", buscar)

elem = "P"
for char in "Ultimate Python":
    print(char)
    if char == elem:
        print(char, elem)
        break
