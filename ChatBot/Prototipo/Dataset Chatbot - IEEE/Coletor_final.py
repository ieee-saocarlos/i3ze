
#DECLARA O QUE É PRECISO PARA FUNCIONAR A BIBLIOTECA

import praw
import time
from langdetect import detect

reddit = praw.Reddit (client_id = 'rhqA-p5KWnpw1w',
                      client_secret = 'Syp0KSiAQi-zWT7_9fP0ZH3924U',
                      username = 'dataset_collector',
                      password = 'jp789521',
                      user_agent = 'data_collectorv1')

#STARTA O TIME

before = time.time()


#DEFINE FUNÇÃO QUE VAI FILTRAR OS TEXTOS (MENOR QUE 240 CARACTERES, EM PORTUGUES, ETC)

def filtrar (texto):

    if len(texto) <= 240  and not texto == '' and detect(texto) == 'pt':

        return True

    else:
        return False

def avaliar_linhas (texto):

    a = 1
    for i in texto:
        if i == '\n':
            a +=1

    return a


#DEFINE AS VARIAVEIS PARA CONTROLE (LIST FROM, LIST TO, ETC)

FROM = []

TO = []

K = 1



#DECLARA O SUBREDDIT

subreddit = reddit.subreddit ('brasil')


#PUXA X POSTS A PARTIR DOS TOP POSTS

top_brasil = subreddit.top(limit = 997)


for post in top_brasil:
    
    contador_conversa = 0
    
    #PUXA O COMENTÁRIO MAIS BEM VOTADO QUE PASSE PELO FILTRO

    try:

        comments = post.comments.list()
            
        #INSERE O POST NO FROM E O COMENTARIO NO TO
        try:

            
            if filtrar(comments[0].body.lower()) and filtrar(post.title.lower()):
                TO.append(comments[0].body.lower())
                FROM.append(post.title.lower())


        except:
            pass

#PUXA TODOS OS COMENTARIOS E REPLIES

        try:
            for comment in comments:

                
                replies = comment.replies.list()

                
                if filtrar(comment.body.lower()) and filtrar(replies[0].body.lower()):
                    TO.append(replies[0].body.lower())
                    FROM.append(comment.body.lower())
                    

            
        except:
            pass

    
        print ('Post número: {}\n'.format(K))
        K = K+1


        if not len(FROM) == len(TO):
            break
        
    except UnicodeEncodeError:
        pass


#CONVERTE AS LISTAS EM TEXTO

TXT_FROM = ''

TXT_TO = ''

##for text in FROM:
##    TXT_FROM = TXT_FROM + text.replace('\n', '') + '\n'
##
##for text in TO:
##    TXT_TO = TXT_TO + text.replace('\n', '') + '\n' 


for i in range(len(TO)):
    TXT_FROM = TXT_FROM + FROM[i].replace('\n', '') +'\n'
    TXT_TO = TXT_TO + TO[i].replace('\n', '') +'\n'

    linhas_to = avaliar_linhas(TXT_TO)
    linhas_from = avaliar_linhas(TXT_FROM)

    if linhas_to != linhas_from:
        break
    

#CRIA OS ARQUIVOS E COLOCA OS TEXTOS NELES

with open ('from.txt', 'w', encoding='utf-8') as f:
    f.write(TXT_FROM.rstrip())

with open ('to.txt', 'w', encoding='utf-8') as t:
    t.write(TXT_TO.rstrip())

#finaliza o tempo

after = time.time()

tempo = after - before

#Informa os parâmetros importantes

print ('Tempo de processamento: {} segundos'.format(tempo))

print ('Conversas obtidas: {}'.format(len(FROM)))
