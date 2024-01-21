# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

# Inicializar contadores
numeros_pares = 0
numeros_impares = 0

# Processo de leitura
while True:
    # Solicitar um número ao usuário
    numero = int(input("Digite um número (digite 0 para encerrar): "))

    # Validar se o número é positivo
    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue

    # Verificar se o número é zero para encerrar o loop
    if numero == 0:
        break

    # Contar números pares e ímpares
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

# Apresentar os resultados
print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")

