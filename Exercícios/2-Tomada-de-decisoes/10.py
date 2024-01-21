# 10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.

# Solicitar três números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Ordenar os números em ordem crescente
lista_numeros = [num1, num2, num3]
lista_numeros.sort()

# Mostrar os números em ordem crescente
print(f"Números em ordem crescente: {lista_numeros}")
