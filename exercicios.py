import random 

# # Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = list(range(0,11))
# for numero in numeros:
#     print(numero**2)


# # Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista = ["Python", "Java", "C++", "JavaScript"]
# lista.pop(2)
# print(lista)
# lista.append("Ruby")
# print(lista)

# # Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# livro: dict = {
#     "titulo": "Harry Potter",
#     "autor": "Fulano",
#     "ano": 2017
# }

# # Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# # Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")

# # 90.Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# # No final, mostre o conteúdo da estrutura na tela.

# aluno = {}

# aluno["Nome"] = input("Nome: ")
# aluno["Média"] = float(input(f"Média de {aluno["Nome"]}: "))
# if aluno["Média"] < 7:
#     aluno["Situacao"] = "Reprovado"
# else:
#     aluno["Situacao"] = "Aprovado"

# for k, v in aluno.items():
#     print(f"{k} é igual a {v}")

# 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultdos aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo 
# que o vencedor tirou o maior número no dado.

jogo = {}

jogo["jogador1"] = random.randint(1, 6)
jogo["jogador2"] = random.randint(1, 6)
jogo["jogador3"] = random.randint(1, 6)
jogo["jogador4"] = random.randint(1, 6)

print("Valores sorteados:")
for k, v in jogo.items():
    print(f"    O {k} tirou {v}")

print("Ranking dos jogadores:")

# Sort based on Values
val_based = {k: v for k, v in sorted(jogo.items(), key=lambda item: item[1])}
# item[1] represents the sorting based on value

# Sort based on reverse of Values
val_based_rev = {k: v for k, v in sorted(jogo.items(), key=lambda item: item[1], reverse=True)}

# Print sorted dictionary
print(val_based)
print(val_based_rev)

