# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha uma opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    return input("Digite o número da opção desejada: ")

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            celsius = float(input("Digite a temperatura em graus Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)
            print(f"A temperatura em Fahrenheit é: {resultado} °F")

        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"A temperatura em Celsius é: {resultado} °C")
            
        else:
            print("Opção inválida. Por favor, escolha outra opção.")

if __name__ == "__main__":
    main()

