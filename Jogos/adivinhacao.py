print('*********************************')
print("Bem-vindo ao jogo de adivinhação!")
print('*********************************')

numero_secreto = 42

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

print('Fim do jogo')
