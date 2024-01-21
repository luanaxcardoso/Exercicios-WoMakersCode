# 4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.

# Solicitar a nota ao usuário
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verificar a nota e classificar o aluno
if nota >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")


