import csv

path = './exemplo.csv'

with open(path, mode="r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)

    for linha in leitor:
        print(linha)