# 1- Faça um Programa que peça dois números e realize as principais operações: soma, subtração, multiplicação, divisão em python

#f é para formatar a string e \n é para pular linha

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2

print(f"\nNúmeros digitados são: {num1} e {num2}")
print(f"\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")
