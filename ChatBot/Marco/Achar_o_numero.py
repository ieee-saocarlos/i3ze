import random

print ('*** Bem vindo ao Acerte o numero!!!')
print ('Voce tem 6 chances e o numero esta entre 0 e 100 !!!!')
continuar = 'sim'

while continuar == 'sim':
    x = random.randrange(100)
    i = 1
    flag = 0
    while i <= 6:
        y = input("Digite sua escolha\n")
        y = int(y)
        if x > y:
            print ('O numero e maior!!')
        elif x < y:
            print ("O numero e menor!!")
        else:
            print ('Parabens, voce acertou!!!')
            flag = 1
            break
        i = i + 1
    if flag != 1:
        print ('Que pena!!! Voce Perdeu >:(')
        print ('O numero era:', x)

    continuar = input('Voce deseja outra partida? [sim/nao]')

