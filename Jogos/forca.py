import random


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta  = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    erros            = 0
    enforcou = False
    acertou  = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):  # Verifica se a letra está correta
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou  = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    print('Fim do jogo')

def carrega_palavra_secreta():
    with open('palavras.txt') as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    # Sorteando a palavra secreta
    numero = random.randrange(0, len(palavras))
    palavra_secreta  = palavras[numero].upper()

    return palavra_secreta

def imprime_mensagem_abertura():
    print('*********************************')
    print("Bem-vindo ao jogo de forcaforca.py!")
    print('*********************************')

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def pede_chute():
    return input('Qual letra? ').strip().upper()

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print('Você ganhou!')

def imprime_mensagem_perdedor():
    print('Você perdeu!')


if(__name__ == '__main__'):
    jogar()
