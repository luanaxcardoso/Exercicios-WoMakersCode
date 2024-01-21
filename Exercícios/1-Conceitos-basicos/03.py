# 3 - Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros

quilometros = float(input("Digite a quantidade de quilômetros: "))
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

#2f é para limitar a quantidade de casas decimais

print(f"\n{quilometros} quilômetros equivalem a:")
print(f"{metros:.2f} metros")
print(f"{centimetros:.2f} centímetros")
print(f"{milimetros:.2f} milímetros")
