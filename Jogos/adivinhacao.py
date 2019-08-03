import random as r


print('*********************************')
print("Bem-vindo ao jogo de adivinhação!")
print('*********************************')

numero_secreto = r.randrange(1, 101)
tentativas     = 3

print('Qual nível de dificuldade?')
print('(1) Fácil\t(2) Médio\t(3) Difícil')

nivel = int(input('Defina o nível: '))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5

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
