## Exercícios

from typing import List

#Vamos revisar funções adicionando type hints e Pydantic
#1. Calcular Média de Valores em uma Lista

def media_lista(valores: list[float]) -> float:
    """
    Calcula e retorna a media aritmetica de todos os valores da lista
    """
    media = sum(valores) / len(valores)
    result = print(f"A média de todos os valores da lista é {media}")
    return result

teste_media = media_lista([10, 5, 8, 9, 10, 3])


#2. Filtrar valores de uma lista que estiveram Acima de um Limite
def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    lista_filtrada = []
    for i in valores:
        if i > limite:
            lista_filtrada.append(i)
    return lista_filtrada

teste_lista = filtrar_acima_de([2, 4, 5, 10, 15, 26], 5)

print(teste_lista)


#3. Contar Valores Únicos em uma Lista

def contar_unicos(valores: list[int]) -> int:
    """
    Conta os valores únicos em uma lista de valores inteiros
    """
    lista_unicos = []
    for i in valores:
        if i not in lista_unicos:
            lista_unicos.append(i)
    return len(lista_unicos)

teste_contar_unicos = contar_unicos([1, 4, 1, 2, 5, 8, 8, 8, 9, 9])

print(teste_contar_unicos)


#4. Converter Celsius para Fahrenheit em uma Lista

def celcius_to_fahrenheit_list(valores: list[float]) -> list[float]:
    """
    Faz a conversão de Celcius para Fahrenheit em cada valor da lista fornecida
    """
    valores_f = []
    for i in valores:
        f = (i * 9/5) + 32
        valores_f.append(f)
    return valores_f

conversor = celcius_to_fahrenheit_list([5, 6, 12, 5.8, 7.9, 12.9])

print(conversor)

#5. Calcular Desvio Padrão de uma Lista

def desvio_padrao(valores: list[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

desvio = desvio_padrao([5, 6, 12, 5.8, 7.9, 12.9])

print(desvio)



#6. Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(valores: list[int]) -> int:
    list_result = []
    menor = min(valores)
    maior = max(valores) + 1
    seq_completa = set(range(menor, maior))
    for valor in seq_completa:
        if valor not in valores:
            list_result.append(valor)
    return list_result

teste = encontrar_valores_ausentes([1, 2, 3, 5, 6, 9])
print(teste)

# Outra forma de resolução:
def encontrar_vlrs_ausentes(valores: list[int]) -> int:
    menor = min(valores)
    maior = max(valores) + 1
    seq_completa = set(range(menor, maior))
    return list(seq_completa - set(valores))

teste2 = encontrar_vlrs_ausentes([1, 2, 3, 5, 6, 9])
print(teste2)
