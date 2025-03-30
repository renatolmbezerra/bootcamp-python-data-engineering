import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> float:
    """
    Soma todos os produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += float(produto.get("price"))
    return valor_total
