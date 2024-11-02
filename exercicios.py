from random import randint
from time import sleep
from operator import itemgetter
from datetime import date

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

# # 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultdos aleatórios.
# # Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo 
# # que o vencedor tirou o maior número no dado.

# jogo = {'jogador1': randint(1, 6), 
#         'jogador2': randint(1, 6), 
#         'jogador3': randint(1, 6), 
#         'jogador4': randint(1, 6)}
# ranking = []

# print("Valores sorteados:")
# for k, v in jogo.items():
#     print(f"    O {k} tirou {v}")
#     sleep(1)

# print("  == RANKING DOS JOGADORES ==")
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
# print('-=' * 30)
# for i, v in enumerate(ranking):
#     print(f"    {i+1}º lugar: {v[0]} com {v[1]}.")
#     sleep(1)

# # 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
# # em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de
# # contratação e o salário. Calcule e acrecente, além da idade, com quantos anos a pessoa vai se
# # aposentar.


# nome = input("Nome: ")
# ano_nasc = int(input("Ano de Nascimento: "))
# ano_atual = date.today().year
# ctps = int(input("Carteira de Trabalho (0 não tem): "))
# idade = ano_atual - ano_nasc

# cadastro = {"Nome": nome, 
#             "idade": idade,
#             "ctps": ctps
#             }
# if ctps != 0:
#     cadastro["contratação"] = int(input("Ano de Contratação: "))
#     cadastro["salario"] = float(input("Salário: "))
#     cadastro["aposentadoria"] = idade + 35

# print("-=" * 30)
# for k, v in cadastro.items():
#     print(f"{k} tem o valor {v}")

# # 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# # do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# # No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o
# # campeonato.

# nome_jogador = input("Nome do jogador: ")
# qtd_partidas = int(input(f"Quantas partidas {nome_jogador} jogou? "))
# gols = []

# for p in range(1, qtd_partidas + 1):
#     gols.append(int(input(f"Quantos gols na partida {p}: ")))

# aproveitamento = {"nome": nome_jogador, "gols": gols, "total": sum(gols)}
# print("-=" * 30)
# print(aproveitamento)

# print("-=" * 30)
# for k, v in aproveitamento.items():
#     print(f"O campo {k} tem o valor {v}.")

# print("-=" * 30)
# print(f"O jogador {nome_jogador} jogou {qtd_partidas} partidas.")

# for i, v in enumerate(gols):
#     print(f"    => Na partida {i}, fez {v} gols.")
# print(f"Foi um total de {sum(gols)} gols.")

# # 94. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# # pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# # a) Quantos pessoas cadastradas.
# # b) A média de idade.
# # c) Uma lista com mulheres.
# # d) Uma lista com idade acima da média

# galera: list = []
# pessoa: dict = {}

# while True:
#     pessoa.clear()
#     pessoa['nome'] = str(input('Nome: '))
#     while True:
#         pessoa['Sexo'] = str(input('Sexo: ')).upper()[0]
#         if pessoa['Sexo'] in 'MF':
#             break
#         print('ERRO! Por favor, digite apenas M ou F.')
#     pessoa['idade'] = int(input('Idade: '))
#     galera.append(pessoa.copy())
#     while True:
#         resp = str(input('Quer continuar? ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print(galera)


estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)