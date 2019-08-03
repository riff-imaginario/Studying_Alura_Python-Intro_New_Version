print('*********************************')
print("Bem-vindo ao jogo de adivinhação!")
print('*********************************')

numero_secreto = 42
tentativas     = 3

for rodada in range(1, tentativas + 1):
    print('Tentativas: {0} de {1}'.format(rodada, tentativas))
    chute = int(input('Digite um número entre 1 e 100: '))

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue  # volta para o início do loop

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print('Você acertou')
        break  # sai do loop
    else:
        if(maior):
            print('Você errou! Seu número foi maior do que o número secreto.')
        elif(chute < numero_secreto):
            print('Você errou! Seu número foi menor do que o número secreto.')

print('Fim do jogo')
