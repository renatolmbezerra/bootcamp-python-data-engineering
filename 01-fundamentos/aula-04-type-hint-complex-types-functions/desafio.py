# Criar uma função, type hint e while para que cada vez que o programa for rodado, adicionar um dicionário a uma lista.


def cadastrar_bonus(nome: str, salario: float, percentual_bonus: float) -> dict:
    """
    Calcula o bônus e retorna um dicionário com nome, salário e valor do bônus.
    """
    valor_bonus = 1000 + salario * (percentual_bonus / 100)
    return {"Nome": nome, "Salario": salario, "Bonus": valor_bonus}

# Lista para armazenar os registros
lista_registros = []

while True:
    # Validação do nome
    nome_valido = False
    while not nome_valido:
        try:
            nome = input("Digite seu nome: ")

            # Verifica se o nome está vazio ou contém números
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                nome_valido = True
        except ValueError as e:
            print(e)

    # Validação do salário
    salario_valido = False
    while not salario_valido:
        try:
            salario = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    # Validação do percentual de bônus
    bonus_valido = False
    while not bonus_valido:
        try:
            percentual_bonus = float(input("Digite o percentual do bônus (%): "))
            if percentual_bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    # Chamada da função e armazenamento dos dados
    registro = cadastrar_bonus(nome, salario, percentual_bonus)
    lista_registros.append(registro)

    # Exibe o resultado para o usuário
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${registro['Bonus']:.2f}.")

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja cadastrar outro bônus? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Exibe todos os registros no final
print("\nRegistros cadastrados:")
for registro in lista_registros:
    print(registro)
