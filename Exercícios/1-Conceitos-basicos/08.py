# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês

# Solicitar ao usuário o valor ganho por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Digite o valor ganho por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcular o salário total
salario_total = valor_por_hora * horas_trabalhadas

# Imprimir o resultado
print(f"O salário total no mês é: R$ {salario_total:.2f}")
