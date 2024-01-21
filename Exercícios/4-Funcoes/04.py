# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

conversao = {
    'Dólar Americano': 4.91,
    'Peso Argentino': 0.02,
    'Dólar Australiano': 3.18,
    'Dólar Canadense': 3.64,
    'Franco Suíço': 0.42,
    'Euro': 5.36,
    'Libra Esterlina': 6.21
}

dinheiro_na_carteira = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

print("\nCom R$ {:.2f} na carteira, você poderia comprar:".format(dinheiro_na_carteira))
for moeda, taxa in conversao.items():
    quantidade = dinheiro_na_carteira / taxa
    print(f"{moeda}: {quantidade:.2f}")
