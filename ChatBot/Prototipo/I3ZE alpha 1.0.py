import os
import time as time
from jogos import achar_o_numero
from jogos import jokenpo

desconsideraveis = ['o', 'os', 'das', 'dos', 'que', 'com','a', 'e', 'no', 'na', 'de', 'do', 'da', 'para', 'pra', 'ate', '', ':d', ':D', ':)', ':(', ';)', ';(', 'se']
acentuaveis = {'á':'a', 'à':'a', 'ã':'a', 'â':'a', 'é':'e', 'è':'e', 'ê':'e', 'í':'i', 'ì':'i', 'î':'i', 'ó':'o', 'ò':'o', 'õ':'o', 'ô':'o', 'ú':'u', 'ù':'u', 'û':'u'}
pontuacao = ['!', '?', '.', ',', ';', ':', "'"]
despedida = ['tchau', 'ate mais', 'falou']


def arrumar(lista):
    lista = lista.lower()

    lista = lista.split(' ')

    for i in desconsideraveis:
        numero = lista.count(i)
        for k in range(numero):
            lista.remove(i)

    for k in range(len(lista)):
        for g in lista[k]:
            if g in pontuacao:
                lista[k] = lista[k].replace(g, "")
                if g == '?':
                    lista.append('?')
            if g in acentuaveis:
                lista[k] = lista[k].replace(g, acentuaveis[g])

    return lista

def abrir_documentos():

    '''with open('teste1.txt', 'r', encoding='utf-8') as inputs1:
        entrada = inputs1.readlines()

    with open('teste2.txt', 'r', encoding='utf-8') as outputs1:
        saida = outputs1.readlines()'''

    with open('from.txt', 'r', encoding='utf-8') as inputs:
        entrada = inputs.readlines()

    with open('to.txt', 'r', encoding='utf-8') as outputs:
        saida = outputs.readlines()

    for k in range(len(entrada)):
        entrada[k] = entrada[k].replace('\n', '')

    for h in range(len(entrada)):
        entrada[h] = arrumar(entrada[h])

    return entrada, saida

def ler_sobre():
    first = 0
    second = 0
    flag = 0
    file = open(os.path.join(os.path.dirname(__file__), 'sobre', 'ieee.txt'), 'r')
    print('O que gostaria de saber sobre o IEEE? \n')

    for line in file:
        if line[2] == '-':
            flag += 1
            print(line)
    print('--------------------------------------------------------------------------------------------------')
    file.seek(0, 0)
    if (flag != 1):
        flag = 0
        first = input('Selecione a opção desejada \n')
        for line in file:
            if line[0] == first and line[3] == '-':
                flag += 1
                print(line[1:])
        file.seek(0, 0)

    if (flag != 1):
        second = input('Selecione a opção desejada')
        for line in file:
            if line[0:2] == first + second and line[4] == '-':
                print(line[3:])
    print('-----------------------------------------------------------------------------------------------------------')
    input('voltando ao menu principal. . .')

    file.close()
    return 0



def jogar():
    escolha = 0
    print('--------------------------------------------------------------------------------------------------------------')
    print('Qual jogo gostaria de jogar?')
    print('1 - Jo ken po')
    print('2 - achar o número')
    print( '--------------------------------------------------------------------------------------------------------------')
    while (escolha != '1' and escolha != '2'):
        escolha = input('Digite o número correspondente à opção selecionada: \n')
    return escolha


'''def conectar():

    print('\nConectando', end="", flush=True)
    print(' .', end="", flush=True)
    time.sleep(0.75)
    print(' .', end="", flush=True)
    time.sleep(0.75)
    print(' .')
    time.sleep(0.75)
    print('')'''

def opções():
    escolha = 0
    print('---------------------------------------------------------------------------------------')
    print('O que gostaria de fazer agora?')
    print('1 - Saber mais sobre o IEEE')
    print('2 - Conversar')
    print('3 - Jogar')
    print('s - Sair')
    print('--------------------------------------------------------------------------------------------------------------')
    while (escolha != '1' and escolha != '2' and escolha != '3' and escolha != 's'):
        escolha = input('Digite o número correspondente à opção selecionada: \n')
    return escolha


def conversar(entrada, saida, nome):
    valor = 0
    while valor == 0:

        resposta = 'nao entendi'

        pergunta = input("{}:\t".format(nome))

        for k in pergunta:
            if k in acentuaveis:
                pergunta = pergunta.replace(k, acentuaveis[k])

        if pergunta.lower() in despedida:
            print('')
            print("I3ze:\tAté mais")
            valor = 1
            return 0

        pergunta = arrumar(pergunta)

        porc = []
        for i in range(len(entrada)):
            porc.append(0.0)
            for k in pergunta:
                if k in entrada[i]:
                    porc[i] = porc[i] + 1
            porc[i] = (2 * porc[i]) / (len(entrada[i]) + len(pergunta))
            #print (entrada[i], porc[i], i, saida[i])

        maior = 0
        for k in range(len(porc)):
            if porc[k] > maior:
                maior = porc[k]
                resposta = str(saida[k])
                if '{}' in resposta:
                    resposta = resposta.format(nome.lower())

        print ('')
        print ("I3ze:\t" + resposta)
        if resposta == 'nao entendi':
            print ("")


def main():

    option = 1

    entrada, saida = abrir_documentos()

    nome = input("Digite seu nome: ")

    #conectar()

    while option != 's':
        escolha = opções()

        if escolha == '1':
           option = ler_sobre()

        elif escolha == '2':
            option = conversar(entrada, saida, nome)

        else:
            jogo = jogar()
            if jogo == '1':
                option = jokenpo()
            if jogo == '2':
                option = achar_o_numero()

if __name__ == '__main__':
    main()