# 2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    
    return int(str(numero)[::-1])


numero_digitado = int(input("Digite um número inteiro: "))


resultado = reverso_numero(numero_digitado)
print(f"O reverso do número {numero_digitado} é: {resultado}")
