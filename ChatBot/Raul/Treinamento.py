import time as time

desconsideraveis = ['o', 'os', 'das', 'dos', 'que', 'com','a', 'e', 'no', 'na', 'de', 'do', 'da', 'para', 'pra', 'ate', '', ':d', ':D', ':)', ':(', ';)', ';(', 'se']
acentuaveis = {'á':'a', 'à':'a', 'ã':'a', 'â':'a', 'é':'e', 'è':'e', 'ê':'e', 'í':'i', 'ì':'i', 'î':'i', 'ó':'o', 'ò':'o', 'õ':'o', 'ô':'o', 'ú':'u', 'ù':'u', 'û':'u'}
pontuacao = ['!', '?', '.', ',', ';', ':', "'"]

fator_prox = 0.8 #fator minito de proximidade

arquivo_from = 'teste1.txt' #arquivo de entrada que vai ser editado
arquivo_to = 'teste2.txt' #arquivo de saida que vai ser editado

def arrumar(lista): #separa as frases em palavras chaves

    lista = lista.replace('\n', '')

    lista = lista.lower()

    lista = lista.split(' ')

    for i in desconsideraveis: #retira as conjuncoes e outros
        numero = lista.count(i)
        for k in range(numero):
            lista.remove(i)

    for k in range(len(lista)): #retira as pontuacoes e acentos
        for g in lista[k]:
            if g in pontuacao:
                lista[k] = lista[k].replace(g, "")
                if g == '?':
                    lista.append('?')
            if g in acentuaveis:
                lista[k] = lista[k].replace(g, acentuaveis[g])

    return lista

with open(arquivo_from, 'r', encoding='utf-8') as ent:
    inputs = ent.readlines()
    ent.close()

with open(arquivo_to, 'r', encoding='utf-8') as sai:
    outputs = sai.readlines()
    sai.close()

entradas = []

for k in inputs: #cria uma lista "arrumada" com o arquivo de entrada, para nao alterar o arquivo original (nao perder as conjuncoes e outros que faziam parte)
    entradas.append(arrumar(k))

for k in range(len(outputs)): #tira os \n e \t das frases completas
    inputs[k] = inputs[k].replace('\n', '')
    inputs[k] = inputs[k].replace('\n', '')
    outputs[k] = outputs[k].replace('\n', '')
    outputs[k] = outputs[k].replace('\t', '')


h = 1
while h == 1:

    pergunta = input('\nDigite a pergunta:\t')

    perg_arrumada = arrumar(pergunta) #arrumar a pergunta

    porc = []
    for i in range(len(entradas)): #comparar a pergunta com a data base de entrada, vendo a proximidade
        porc.append(0.0)
        for k in perg_arrumada:
            if k in entradas[i]:
                porc[i] = porc[i] + 1
        porc[i] = (2 * porc[i]) / (len(entradas[i]) + len(perg_arrumada))

    maior = 0.0
    for k in range(len(porc)): #seleciona qual entrada esta acima do valor de proximidade dado e pega qual a maior proxima
        if porc[k] >= fator_prox:
            if porc[k] > maior:
                maior = porc[k]

    if maior == 0: #se nao tem nenhuma entrada proxima o suficiente

        print('\nNao há resposta para essa pergunta')

        p = 0
        while p == 0:
            resp = input('Digite a resposta para essa pergunta:\t')

            inputs.append(pergunta)
            entradas.append(perg_arrumada)
            outputs.append(resp)
            print ('--- ADICIONADO ---') #adiciona a resposta para a pergunta existente, adicionando a pergunta na lista "arrumada" e na original (para escrever no novo arquivo)

            esc = input('Deseja adicionar outra resposta para essa pergunta?\t')

            if esc != 'sim': #se nao quer adicionar mais respostas possiveis para a pergunta
                p = 1

    else:

        escolha = input('\nEssa frase esta na data base, voce deseja apaga-la?\t')

        if escolha != 'sim': #se a entrada existe (suficientemente proxima a pergunta) e se nao quer deletar essa entrada da data base

            valores = []
            for k in range(len(porc)): #seleciona as posicoes de todas as entradas com esse nome
                if porc[k] == maior:
                    valores.append(k)

            print ('A pergunta apresenta as seguintes perguntas:')

            a = 0
            quant = []

            for k in valores: #printa todas as respostas que existem para a entrada e coloca cada uma delas ligadas a um numero na matriz quant
                a = a + 1
                print ('({})\t'.format(a), outputs[k])
                quant.append([a, k])

            escolhinha = input('Todas essas respostas sao boas?\t')

            if escolhinha != 'sim': #se alguma das respostas nao esta boa o suficiente

                p = 1

                while p == 1:

                    qual = int(input('Digite o numero correspondente a resposta errada\t'))

                    for i in quant:
                        if i[0] == qual: #ve qual o numero correspondente a repsosta foi selecionada para editar

                            delet = input('Voce deseja deletar essa resposta?\t')

                            if delet != 'sim': #se nao quer deletar a resposta, so edita ela
                                resp = input('Entao digite a resposta a ser adicionada a essa pergunta:\t')
                                print ('--- ADICIONADO ---')
                                outputs[i[1]] = resp

                            else: #se quiser deletar a resposta, deleta a resposta e as entradas na lista origial e "arrumada"
                                del inputs[i[1]]
                                del outputs[i[1]]
                                del entradas[i[1]]
                                for j in range(len(valores)):
                                    if valores[j] > i[1]: #se retirar uma resposta que esta acima das outras, tira uma posicao, porque as outras respostas/entradas vao subir uma posicao
                                        valores[j] = valores[j] - 1
                                valores.remove(i[1])

                                print ('--- DELETADO ---')

                    print('A pergunta apresenta as seguintes perguntas:')

                    a = 0
                    quant = []

                    for k in valores: #mesma coisa ali em cima
                        a = a + 1
                        print('({})\t'.format(a), outputs[k])
                        quant.append([a, k])

                    e = input('Todas as respostas estao boas agora?\t')

                    if e == 'sim': #se nao quer mais editar mais nenhuma resposta, sai do loop
                        p = 0

            esc = input('Deseja adicionar outra resposta para essa pergunta?\t')

            if esc == 'sim': #se quiser adicionar outra resposta possivel

                p = 0
                while p == 0:

                    resp = input('Digite a resposta para essa pergunta:\t')

                    inputs.append(pergunta)
                    entradas.append(perg_arrumada)
                    outputs.append(resp)
                    print ('--- ADICIONADO ---') #adiciona a pergunta, a pergunta "arrumada" e a resposta digitada nas listas

                    esc = input('Deseja adicionar outra resposta para essa pergunta?\t')

                    if esc != 'sim': #se nao quer mais adicionar pergunta, sai do loop
                        p = 1

        else: #se quiser apagar a pergunta e todas as respostas possiveis para a pergunta

            vez = 0

            valores = []
            for k in range(len(porc)): #verifica as posicoes das perguntas e respostas
                if porc[k] == maior:
                    valores.append(k)

            for k in valores: #deleta todas as posicoes encontradas, sendo que cada vez que deleta, a proxima posicao diminui um, por tirar uma posicao anterior
                del outputs[k-vez]
                del inputs[k-vez]
                del entradas[k-vez]
                print('--- DELETADO ---')
                vez = vez + 1 #conta as vezes que deletou para diminuir a posicao que tinha encontrad

    saida = input('\n   Voce deseja finalizar o ensino e salvar as mudancas?\t')
    if saida == 'sim': #se nao quer mais editar a data base, sai do loop
        h = 0


with open(arquivo_from, 'w', encoding='utf-8') as from_saida: #escreve o arquivo de texto da data base de entrada
    for k in range(len(inputs)):
        if k == len(inputs) - 1:
            from_saida.write(inputs[k])
            continue
        from_saida.write(inputs[k] + '\n')

    from_saida.close()

with open(arquivo_to, 'w', encoding='utf-8') as to_saida: #escreve o arquivo de texto da data base de saida
    for k in range(len(outputs)):
        if k == len(outputs) - 1:
            to_saida.write(outputs[k])
            continue
        to_saida.write(outputs[k] + '\n')

    to_saida.close()
