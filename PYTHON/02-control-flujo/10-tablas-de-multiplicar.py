## EJERCICIO 1
## Crea un programa que solicite al usuario un número del 1 al 10 y muestre por pantalla la tabla de multiplicación del 1 al 10

num = int(input("Digite el numero del 1 al 10 devolver su tabla: "))


def tablas(num):
    for multiplo in range(1, 11):
        print(f"{num} x {multiplo} = {num * multiplo}")


tablas(num)


## EJERCICIO 2
## Crea un programa que solicite al usuario dos números enteros y muestre por pantalla
## el resultado de las siguientes operaciones: suma, resta, multiplicación y división.

## Calculadora - 01.08-calculadora.py
