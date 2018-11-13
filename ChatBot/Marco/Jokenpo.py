import random

continuar = 'sim'
b=['pedra', 'tesoura', 'papel']
print (" ******* BEM VINDO AO JOKENPO!! ****** ")

while (continuar == 'sim'):
    j1 = input("Por favor, escolha sua jogada e digite-a! [pedra/papel/tesoura]\n")
    j2 = random.choice (b)
    print ('A escolha do Jogador 2 foi:', j2)

    if (j1==j2):
        print ('Nenhum vencedor!!! Tente outra vez.\n')
    if (j1=='pedra') :
        if ( j2 == 'tesoura'):
            print ("Jogador 1 venceu!!! Parabens!!!\n")
        elif ( j2=="papel"):
            print ("Jogador 2 venceu. Tente outra vez!!!\n")
    elif (j1=='papel') :
        if ( j2=='pedra'):
            print ('Jogador 1 venceu. Parabens!!!\n')
        elif ( j2=="tesoura"):
            print ( "Jogador 2 venceu. Tente outra vez !!!\n")
    else :
        if ( j2=='pedra'):
            print ("Jogador 2 venceu. Tente outra vez!!!\n")
        elif ( j2=='papel'):
            print ("Jogador 1 venceu. Parabens !!!\n ")

    continuar = input ("Deseja outra partida? [sim/nao]\n")


