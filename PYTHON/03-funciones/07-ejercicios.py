# Define una funcion que verifique palindromos

def es_palindromo(text):
    text = erase_space(text)
    new_text = reverse2(text)
    return new_text.lower() == text.lower()


def erase_space(text):
    newText = ""
    for char in text:
        if char != " ":
            newText += char

    return newText


def reverse(text):
    newText = ""
    length = len(text)-1

    for _ in text:
        if length >= 0:
            newText += text[length]
            length = length - 1

    return newText


def reverse2(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text

    return reverse_text

# print("Amo la Paloma", erase_space("Amo la Paloma"))
# print("Hola mundo", reverse("Hola mundo"))


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la Paloma", es_palindromo("Amo la Paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))

# print("Hola mundo".replace(" ", ""))
# print("HOla MunDo".lower().replace(" ", ""))

text = "Amo la Paloma"
newText = text.lower().replace(" ", "")

# print((text[12]), len(newText))
