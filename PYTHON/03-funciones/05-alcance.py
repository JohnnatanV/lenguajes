saludo = "Hola Global"


def saludar():
    saludo = "Hola mundo"
    print(saludo)


def saludoBonito():
    saludo = "Hola mi niña Kelly"
    print(saludo)


print(saludo)  # Recomendacion por buenas practicas no usar variables globales

saludar()
saludoBonito()

# Ejemplo practico de porque no se pueden usar las variables globales

dato = 25


def calcular():
    global dato  # Asigna la variable dentro del contexto como una variable global lo que afecta toda la operacion
    dato = "numero ramdon"


def recalcular():
    dato = 20
    print(dato)


resultado1 = dato + 10
print(resultado1)
calcular()
resultado2 = dato + 15
print(resultado2)
recalcular()
resultado3 = dato - 10
print(resultado3)
