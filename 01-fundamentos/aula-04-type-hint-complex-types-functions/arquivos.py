import csv

# Caminho para o arquivo CSV
caminho_arquivo: str = "exemplo.csv"

# Lista para armazenar os dados
dados = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)

    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        dados.append(linha)

# Exibe os dados contidos na lista índice a índice 
for v in dados:
    print(v)

