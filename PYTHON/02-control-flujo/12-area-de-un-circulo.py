## Ejercicio 3
## Crea un programa que solicite al usuario el radio de un círculo y calcule el área.
## Nota: Utiliza 3.14159 como número PI para el cálculo del área.

radio = int(input("Digite el radio del circulo: "))


def areaCirculo(radio):
    pi = 3.14159
    print(f"{pi * (radio**2)}")


areaCirculo(radio)
