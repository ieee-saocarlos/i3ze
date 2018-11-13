
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


#DEFINE AS VARIAVEIS PARA CONTROLE (LIST FROM, LIST TO, ETC)

FROM = []

TO = []

K = 1

tempo_replies = 0

tempo_comments = 0


#DECLARA O SUBREDDIT

subreddit = reddit.subreddit ('brasil')


#PUXA X POSTS A PARTIR DOS TOP POSTS

top_brasil = subreddit.top(limit = 1500)


for post in top_brasil:
    
    contador_conversa = 0
    
    #PUXA O COMENTÁRIO MAIS BEM VOTADO QUE PASSE PELO FILTRO

    try:

        soltar_comments = time.time()
        comments = post.comments.list()
        puxou_comments = time.time()

        tempo_comments = tempo_comments +  puxou_comments - soltar_comments

            
        #INSERE O POST NO FROM E O COMENTARIO NO TO
        try:

            
            if filtrar(comments[0].body.lower()) and filtrar(post.title.lower()):
                TO.append(comments[0].body.lower())
                FROM.append(post.title.lower())
                contador_conversa = 1


        except:
            pass

#PUXA TODOS OS COMENTARIOS E REPLIES

        try:
            for comment in comments:

                
                soltar_replies = time.time()
                replies = comment.replies.list()
                puxou_replies = time.time()

                tempo_replies = tempo_replies +  puxou_replies - soltar_replies


                
                if filtrar(comment.body.lower()) and filtrar(replies[0].body.lower()):
                    contador_conversa += 1
                    TO.append(replies[0].body.lower())
                    FROM.append(comment.body.lower())
                    

            
        except:
            pass

        
        after_infor = time.time()
        print ('Post número: {}\nTempo decorrido: {} s'.format(K, after_infor - before))
        K = K+1
        print ('Esse post tem {} comentarios'.format(len(comments)))
        print ('tivemos {} conversas que passaram pelo filtro'.format(contador_conversa))
        print (20*'-')

        
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

print ('Tempo de download dos replies: {} segundos'.format(tempo_replies))

print ('Tempo de download dos comentarios: {} segundos'.format(tempo_comments))
