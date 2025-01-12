# print("Hola mundo!")

def hola():
    print("Hola mundo!")
    print("Ultimate Python")


# hola()


def suma(a, b):
    return (a+b)


def resta(a, b):
    print(a - b)


def multi(a, b):
    print(a * b)


def div(a, b):
    print(a / b)


a = 10
b = 11

# suma()


def factorial(num):
    if num == 1:
        return num
    else:
        num = num * factorial(num-1)
        return num


result = factorial(4)
print(result)

print("dat = suma(2,3)")
dat = suma(2, 3)
print(dat * suma(2, 3))

print(2300000*12)
