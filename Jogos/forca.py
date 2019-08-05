import random


def jogar():
    print('*********************************')
    print("Bem-vindo ao jogo de forcaforca.py!")
    print('*********************************')

    arquivo  = open('palavras.txt', 'r')
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()

    # Sorteando a palavra secreta
    numero = random.randrange(0, len(palavras))
    palavra_secreta  = palavras[numero].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]
    erros            = 0
    enforcou = False
    acertou  = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input('Qual letra? ').strip().upper()

        index = 0

        if(chute in palavra_secreta):  # Verifica se a letra está correta
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou  = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu!')

    print('Fim do jogo')


if(__name__ == '__main__'):
    jogar()
