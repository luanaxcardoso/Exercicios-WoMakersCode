# 7. Desenvolver um programa que solicite a idade do usuário e identifique se # ele é uma criança, um adolescente, adulto ou idoso.

# Solicitar a idade ao usuário
idade = int(input("Digite a sua idade: "))

# Identificar a faixa etária
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma criança.")
elif 13 <= idade <= 17:
    print("Você é um adolescente.")
elif 18 <= idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
