print('*********************************')
print("Bem-vindo ao jogo de adivinhação!")
print('*********************************')

numero_secreto = 42
tentativas     = 3
rodada         = 1

while(rodada <= tentativas):
    print('Tentativas: {0} de {1}'.format(rodada, tentativas))
    chute = int(input('Digite o seu número: '))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print('Você acertou')
    else:
        if(maior):
            print('Você errou! Seu número foi maior do que o número secreto.')
        elif(chute < numero_secreto):
            print('Você errou! Seu número foi menor do que o número secreto.')

    rodada     += 1

print('Fim do jogo')
