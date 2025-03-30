import pandas as pd
import os
import glob

# Uma função de extract que le e consolida os json

def extrair_dados_e_consolidando(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_final = pd.concat(df_list, ignore_index=True)
    return df_final


# Uma funcao que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# Uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametro para definir se saida em "csv", "parquet" ou "os dois"
    """
    for format in format_saida:
        if format == 'csv':
            df.to_csv("dados.csv", index=False)
        if format == 'parquet':
            df.to_parquet("dados.parquet")

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidando(pasta)
    data_frame_final = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_final, formato_de_saida)

    

# Bloco de teste
if __name__ == "__main__":
    pasta_argumento: str = 'data'
    data_frame = extrair_dados_e_consolidando(pasta=pasta_argumento)
    data_frame_final = calcular_kpi_de_total_de_vendas(data_frame)
    formato_de_saida = ["csv", "parquet"]
    data_frame_calculado = carregar_dados(data_frame_final, formato_de_saida)
