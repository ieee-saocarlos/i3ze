from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import wikipedia
from googlesearch import search
import webbrowser


#read_only = True


wikipedia.set_lang('pt')   #Colocar para procurar em Portugues

phrase_search_wikipedia = ['Quem e','quem e','O que e','o que e','Definicao de ','definicao de','Qual a definicao de','qual a definicao de','Quem foi',
                           'quem foi','inventor','Inventor','onde fica','Onde fica','quem inventou','Quem inventou']

phare_search_google = ['pesquisar por','Pesquisar por','pesquise por','Pesquise por','pesquise','Pesquise','ache por','Ache por','achar','Achar','procure por',
                       'Procure por','procurar','Procurar']


#FUNCAO PARA PESQUISA NA WIKIPEDIA

def Wikipedia_search(text):
    result = None
    for i in phrase_search_wikipedia:
        if text.startswith(i):
            result = text.replace(i, '')

    if result is not None:
        results = wikipedia.search(result)
        result = wikipedia.summary(results[0],sentences=5)

    return  result


#FUNCAO PARA PESQUISA NO GOOGLE

def Google_search(text):
    result = None
    if text is not None:
        for i in phare_search_google:
            if text.startswith(i):
                result = text.replace(i, '')

        if result is not None:
            for url in search(text, stop=3):
                webbrowser.open_new_tab(url)
                break
            return 'Pesquisa feita com sucesso ->' + result.rstrip()
    return result


#CRIAR CHAT BOT
bot = ChatBot('Jorgin')


#TREINAR BOT
bot.set_trainer(ListTrainer)
for x in os.listdir('Conversas'):
    chat = open('Conversas/' + x,'r').readlines()   # Concatenar pasta com arquivo.txt
    bot.train(chat)



#EXECUTAR A CONVERSA

while True:
    try:

        me = raw_input('Eu: ')

        resposta = Wikipedia_search(me)
        if resposta == None:
            resposta = Google_search(me)
            if resposta == None:
                resposta = bot.get_response(me)

        print 'Jorgin:', resposta

    except(KeyboardInterrupt,EOFError,SystemExit):
        break










