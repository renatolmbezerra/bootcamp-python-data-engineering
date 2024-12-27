import csv

path = './exemplo.csv'

with open(path, mode="r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    cabecalho = next(leitor)
    print(cabecalho)

    for linha in leitor:
        print(linha)