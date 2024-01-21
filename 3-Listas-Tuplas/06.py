# 6. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite o seu nome: ")

nome_maiusculo = nome.upper()

lista_letras = list(nome_maiusculo)

lista_letras.reverse()

nome_invertido = ''.join(lista_letras)

print(f"Nome invertido: {nome_invertido}")
