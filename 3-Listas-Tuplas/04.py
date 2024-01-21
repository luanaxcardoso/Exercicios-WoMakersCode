# 4. Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = [
    ["Paula", "12-685967222"],
    ["Bruno", "12-987654321"],
    ["Carlos", "12-96585543"],
    ["Joao", "12-98556853"]
]

nome = input("Digite o nome do contato que você está procurando: ")

telefone = None

for contato in contatos:
    if contato[0].lower() == nome.lower():
        telefone = contato[1]
        break

if telefone:
    print(f"Telefone de {nome}: {telefone}")
else:
    print(f"Contato com o nome {nome} não foi encontrado.")