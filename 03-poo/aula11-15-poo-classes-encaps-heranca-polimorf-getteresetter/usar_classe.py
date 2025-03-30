from src.interface.classes.csv_class import CsvProcessor


arquivo_csv = './exemplo.csv'
coluna = 'estado'
atributo = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(coluna,atributo))
print(arquivo_CSV.sub_filtro('preço','10,50'))
print('############################')


arquivo_csv2 = './exemplo2.csv'
coluna2 = 'estado'
atributo2 = 'DF'

arquivo_CSV2 = CsvProcessor(arquivo_csv2)
arquivo_CSV2.carregar_csv()
print(arquivo_CSV2.filtrar_por(coluna2,atributo2))