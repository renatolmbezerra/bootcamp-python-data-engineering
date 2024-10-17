CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o percentual do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o seu bônus: ")) / 100

# 4) Calcule o valor do bônus final
kpi = CONSTANTE_BONUS + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"Olá {nome_usuario}, o seu valor bônus foi de {kpi}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?