# 1- Faça um Programa que peça dois números e realize as principais operações: soma, subtração, multiplicação, divisão em python

#Para mudar a cor das frases no terminal usei o Colorama
#Para instalar o Colorama
#pip install colorama
#pip install colorama --user

import colorama

colorama.init()

num1 = int(input( colorama.Fore.CYAN + "Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2

print(colorama.Fore.LIGHTYELLOW_EX + f"\nNúmeros digitados são: {num1} e {num2}")
print(colorama.Fore.MAGENTA + f"\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")
