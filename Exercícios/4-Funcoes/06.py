# 6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista. A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. Dica: Você precisará importar uma biblioteca. 

import random

palavras = ["biblioteca", "python", "mulheres", "desenvolvimento", "tecnologia"]

def escolher_palavra():
    return random.choice(palavras)

def inicializar_palavra_secreta(palavra):
    return ["_" if letra.isalpha() else letra for letra in palavra]

def exibir_palavra_secreta(palavra_secreta):
    print(" ".join(palavra_secreta))

def jogo_forca():
    palavra_secreta = list(escolher_palavra().lower())
    palavra_revelada = inicializar_palavra_secreta(palavra_secreta)
    tentativas_maximas = 6
    tentativas = 0
    letras_tentadas = set()

    while tentativas < tentativas_maximas:
        exibir_palavra_secreta(palavra_revelada)
        letra = input("Digite uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_tentadas:
                print("Tente outra letra!")
            else:
                letras_tentadas.add(letra)
                if letra in palavra_secreta:
                    print("Letra correta!")
                    for i, char in enumerate(palavra_secreta):
                        if char == letra:
                            palavra_revelada[i] = letra
                else:
                    tentativas += 1
                    print(f"Letra incorreta! Tentativas restantes: {tentativas_maximas - tentativas}")

        else:
            print("Entrada inválida. Digite apenas uma letra.")

        if "_" not in palavra_revelada:
            print("Parabéns! Você acertou a palavra secreta!")
            break

    else:
        print(f"Você perdeu! A palavra secreta era: {''.join(palavra_secreta)}")

if __name__ == "__main__":
    jogo_forca()
