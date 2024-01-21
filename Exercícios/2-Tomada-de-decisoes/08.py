# 8. Criar um programa em Python que solicite três números ao usuário, utilize
# estruturas condicionais para determinar o maior entre eles e apresente o
# resultado.

# Solicitar três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Determinar o maior número usando condições
if numero1 > numero2 and numero1 > numero3:
    maior_numero = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

# Apresentar o resultado
print(f"O maior número é: {maior_numero}")
