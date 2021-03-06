
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

    if len(texto) <= 240 and not texto == '[deleted]' and not texto == '' and detect(texto) == 'pt':

        return True

    else:
        return False


#DEFINE AS VARIAVEIS PARA CONTROLE (LIST FROM, LIST TO, ETC)

FROM = []

TO = []

K = 1

#DECLARA O SUBREDDIT

subreddit = reddit.subreddit ('brasil')

#PUXA X POSTS A PARTIR DOS TOP POSTS

top_brasil = subreddit.top(limit = 10
                           )

for post in top_brasil:
    

    #PUXA O COMENTÁRIO MAIS BEM VOTADO QUE PASSE PELO FILTRO

    try:
        comments = post.comments.list()
        
        #INSERE O POST NO FROM E O COMENTARIO NO TO
        try:
            
            if filtrar(comments[0].body.lower()):
                TO.append(comments[0].body.lower())
                FROM.append(post.title.lower())

        except:
            pass

#PUXA 1 REPLY DO COMENTARIO

        replies = comments[0].replies.list()

#ADICIONA O COMENTARIO NO FROM E REPLY NO TO

        try:
        
            if filtrar(comments[0].body.lower()) and filtrar(replies[0].body.lower()):
                TO.append(replies[0].body.lower())
                FROM.append(comments[0].body.lower())

        except:
            pass

#PUXA N CAMADAS DE COMENTARIOS E REPLIES

##        if len(comments) >= 100:
##
##            print('Tem menos de 100 comments')
##            try:
##            
##                for i in range (1,100):
##
##                    replies = comments[i].replies.list()
##                    
##                    if filtrar(comments[i].body.lower()) and filtrar(replies[0].body.lower()):
##                        TO.append(replies[0].body.lower())
##                        FROM.append(comments[i].body.lower())
##
##            except:
##                pass
##        
##        else:

        try:

            opa = 0
            for i in range (1, len(comments)):
 
                replies = comments[i].replies.list()

                if filtrar(comments[i].body.lower()) and filtrar(replies[0].body.lower()):
                    TO.append(replies[0].body.lower())
                    FROM.append(comments[i].body.lower())
                    opa += 1

            
        except:
            pass

        
        after_infor = time.time()
        print ('Post número: {}\nTempo decorrido: {} s'.format(K, after_infor - before))
        K = K+1
        print ('Esse post tem {} comentarios'.format(len(comments)))
        print ('tivemos {} conversas que passaram pelo filtro'.format(opa))

        
    except UnicodeEncodeError:
        pass


#CONVERTE AS LISTAS EM TEXTO

TXT_FROM = ''

TXT_TO = ''

for text in FROM:
    TXT_FROM = TXT_FROM + text.replace('\n', '') + '\n' 

for text in TO:
    TXT_TO = TXT_TO + text.replace('\n', '') + '\n' 

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
