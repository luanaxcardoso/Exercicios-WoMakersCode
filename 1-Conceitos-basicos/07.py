# 7- Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal(IMC)usando a fórmula:IMC=peso/(altura x altura)


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

print(f"O Índice de Massa Corporal (IMC) é: {imc:.2f}")
