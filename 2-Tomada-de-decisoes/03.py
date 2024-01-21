# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    # Solicitar uma nota ao usuário
    nota = float(input("Digite uma nota entre zero e dez: "))

    # Verificar se a nota é válida
    if 0 <= nota <= 10:
        break  # Sair do loop se a nota for válida
    else:
        print("Valor inválido. Por favor, digite uma nota entre zero e dez.")

# Se chegou aqui, a nota é válida
print(f"A nota inserida foi: {nota}")
