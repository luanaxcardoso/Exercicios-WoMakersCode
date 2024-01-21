# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resultado = soma(num1, num2, num3)
print(f"A soma dos três números é: {resultado}")
