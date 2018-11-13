import praw
import time

reddit = praw.Reddit (client_id = 'rhqA-p5KWnpw1w',
                      client_secret = 'Syp0KSiAQi-zWT7_9fP0ZH3924U',
                      username = 'dataset_collector',
                      password = 'jp789521',
                      user_agent = 'data_collectorv1')


subreddit = reddit.subreddit ('brasil')

top_brasil = subreddit.top(limit = 5)

before = time.time()

k = 1

match_comment = 0

match_reply = 0

FROM = []

TO = []


###Puxando os posts do subreddit
for post in top_brasil:
    try:
        print('Post número: {}'.format(k))
        print (post.title)
        print ('\nComentários:\n')
        
        k += 1

        ###Puxando os comentários de cada post
        comments = post.comments.list()

        lenght_comment = len(comments)
        
        if lenght_comment >= 5:
            
            for i in range (5):
                try:
                    if len(comments[i].body) <= 240:
                        print ('Comment {}: '.format(i) + comments[i].body)
                        print(20*'-')
                        match_comment += 1
                        FROM.append(post.title)
                        TO.append(comments[i].body)
                        
                    ###Puxando os replies de cada comentário
                    replies = comments[i].replies.list()
                    lenght = len(replies)

                    if lenght >= 5:
                        for n in range(5):
                            try:
                                if len(replies[n].body) <= 240:
                                    print ('Reply {}: '.format(n)+replies[n].body)
                                    print(10*'-')
                                    match_reply += 1
                                    FROM.append(comments[i].body)
                                    TO.append(replies[n].body)

                                    
                            except AttributeError:
                                pass
                    else:
                        for n in range(lenght):
                            try:
                                if len(replies[n].body) <= 240:
                                    print ('Reply {}: '.format(n)+replies[n].body)
                                    print(10*'-')
                                    match_reply += 1
                                    FROM.append(comments[i].body)
                                    TO.append(replies[n].body)
                                    
                            except AttributeError:
                                pass
                            
                    
                except UnicodeEncodeError:
                    pass
            

            print (50*'-')
                
        else:

            for i in range(lenght_comment):
                try:
                    if len(comments[i].body) <= 240:
                        print ('Comment {}: '.format(i) + comments[i].body)
                        print(20*'-')
                        match_comment += 1
                        FROM.append(post.title)
                        TO.append(comments[i].body)

                    ###Puxando os replies de cada comentário
                    replies = comments[i].replies.list()
                    lenght = len(replies)

                    if lenght >= 5:
                        for n in range(5):
                            try:
                                if len(replies[n].body) <= 240:
                                    print ('Reply {}: '.format(n)+replies[n].body)
                                    print(10*'-')
                                    match_reply += 1
                                    FROM.append(comments[i].body)
                                    TO.append(replies[n].body)
                                    
                                    
                            except AttributeError:
                                pass
                    else:
                        for n in range(lenght):
                            try:
                                if len(replies[n].body) <= 240:
                                    print ('Reply {}: '.format(n)+replies[n].body)
                                    print(10*'-')
                                    match_reply += 1
                                    FROM.append(comments[i].body)
                                    TO.append(replies[n].body)
                                    
                            except AttributeError:
                                pass
                            
                    
                except UnicodeEncodeError:
                    pass
            

            print (50*'-')






            
    except UnicodeEncodeError:
        pass
    
after = time.time()

print (after-before)
print (match_reply)
print (match_comment)
print ('Total Matches: {}'.format(match_comment+match_reply))

TXT_FROM = ''

TXT_TO = ''

for text in FROM:
    TXT_FROM = TXT_FROM + '\n' + text

for text in TO:
    TXT_TO = TXT_TO + '\n' + text

with open ('from.txt', 'w') as f:
    f.write(TXT_FROM)

with open ('to.txt', 'w') as t:
    t.write(TXT_TO)


