# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros = list(range(0,11))
for numero in numeros:
    print(numero**2)


# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]
lista.pop(2)
print(lista)
lista.append("Ruby")
print(lista)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro: dict = {
    "titulo": "Harry Potter",
    "autor": "Fulano",
    "ano": 2017
}

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.