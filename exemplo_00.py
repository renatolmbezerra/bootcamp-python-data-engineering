valor_1 = 4
valor_2 = 6

valor_3 = valor_1 + valor_2

valor_4 = 6
valor_5 = 4

valor_6 = valor_4 + valor_5

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma funcao simples de soma de valores tipo float que retorna float
    """
    Resultado_da_soma = valor_1_para_somar * valor_2_para_somar
    return Resultado_da_soma

teste1 = soma(valor_1, valor_2)

print(teste1)





