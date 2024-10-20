import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
result = n1 + n2
print(result)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
n = int(input("Informe um número inteiro: "))
result = n % 5
print(result)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
result = n1 * n2
print(result)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
result = n1 // n2
print(result)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
n = int(input("Informe um número inteiro: "))
result = n ** 2
print(result)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
result = n1 + n2
print(result)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
result = (n1 + n2) / 2
print(result)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
n1 = int(input("Informe um número base: "))
n2 = int(input("Informe outro número para o expoente: "))
result = n1 ** n2
print(result)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temp = float(input("Informe a temperatura em celsios: "))
result =(temp * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é de: {result}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o valor do raio para calcular a área do círculo: "))
area = math.pi * (raio ** 2)
print(f"{area:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Escreva um texto: ")
print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
nome = nome.lower()
print(nome)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Escreve uma frase: ")
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
print(data.split("/"))

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = input("Digite a primeira palavra: ")
str2 = input("Digite a segunda palavra: ")
juncao = str1 + " " + str2
print(juncao)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação