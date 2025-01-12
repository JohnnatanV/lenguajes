bienvenida = """
Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, multi, div y resta
"""

# n1 = input("Ingresa numero: ")
# n2 = input("Ingresa siguiente numero: ")
# operacion = input("Ingresa operacion: ")

# n1 = int(n1)
# n2 = int(n2)
# suma = f"""El resultado es {n1 + n2}"""
# resta = f"""El resultado es {n1 - n2}"""
# multi = f"""El resultado es {n1 * n2}"""
# div = f"""El resultado es {n1 / n2}"""

# print(n1, n2)
# calc = True
print(bienvenida)

res = ""
# n1 = int(n1)
while True:
    if not res:
        res = input("Ingresa numero: ")
        if res.lower() == "salir":
            break
        res = int(res)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        res += n2
    elif op.lower() == "resta":
        res -= n2
    elif op.lower() == "multi":
        res *= n2
    elif op.lower() == "div":
        res /= n2
    else:
        print("Operacin no valida")
        break

    print(f"""El resultado es {res}""")


#        if operacion.lower == "suma":
#            operacion = input("Ingresa operacion: ")
#            n2 = input("Ingresa siguiente numero: ")
#            n2 = int(n2)
#            suma = n1 + n2
#            print(f"""El resultado es {suma}""")
#            n1 = suma
#        elif operacion == "resta":
#            operacion = input("Ingresa operacion: ")
#            n2 = input("Ingresa siguiente numero: ")
#            n2 = int(n2)
#            resta = n1 - n2
#            print(f"""El resultado es {resta}""")
#            n1 = resta
#        elif operacion == "multi":
#            operacion = input("Ingresa operacion: ")
#            n2 = input("Ingresa siguiente numero: ")
#            n2 = int(n2)
#            multi = n1 * n2
#            print(f"""El resultado es {multi}""")
#            n1 = multi
#        else:
#            operacion = input("Ingresa operacion: ")
#            n2 = input("Ingresa siguiente numero: ")
#            n2 = int(n2)
#            div = n1 - n2
#            print(f"""El resultado es {div}""")
#            n1 = div
#
