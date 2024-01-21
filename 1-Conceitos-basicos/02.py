# 2- Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print(f"\nVocê tem {idade} anos de idade.")
