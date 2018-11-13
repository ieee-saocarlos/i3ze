import time as time

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

    with open('teste1.txt', 'r', encoding='utf-8') as inputs1:
        entrada = inputs1.readlines()

    #with open('from.txt', 'r', encoding='utf-8') as inputs:
    #    entrada = inputs.readlines()

    with open('teste2.txt', 'r', encoding='utf-8') as outputs1:
        saida = outputs1.readlines()

    #with open('to.txt', 'r', encoding='utf-8') as outputs:
    #    saida = outputs.readlines()

    for k in range(len(entrada)):
        entrada[k] = entrada[k].replace('\n', '')

    for h in range(len(entrada)):
        entrada[h] = arrumar(entrada[h])


    return entrada, saida


def conectar():

    print('\nConectando', end="", flush=True)
    print(' .', end="", flush=True)
    time.sleep(0.75)
    print(' .', end="", flush=True)
    time.sleep(0.75)
    print(' .')
    time.sleep(0.75)
    print('')


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
            break

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


###########################################################################################

entrada, saida = abrir_documentos()

nome = input("Digite seu nome: ")

conectar()

conversar(entrada, saida, nome)
