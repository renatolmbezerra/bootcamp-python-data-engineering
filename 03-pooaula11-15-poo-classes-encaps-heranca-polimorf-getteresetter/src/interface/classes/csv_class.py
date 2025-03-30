import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df


    def filtrar_por(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado

    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]
