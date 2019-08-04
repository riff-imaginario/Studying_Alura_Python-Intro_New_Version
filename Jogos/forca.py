def jogar():
    print('*********************************')
    print("Bem-vindo ao jogo de forcaforca.py!")
    print('*********************************')

    palavra_secreta = 'banana'

    enforcou = False
    acertou  = False

    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                print('Encontrei a letra {} na posição {}'.format(letra, index))
            index += 1


    print('Fim do jogo')


if(__name__ == '__main__'):
    jogar()
