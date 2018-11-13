#recebe o texto e a database

def avaliar_texto (texto, FROM, TO):
    
#Criar as variáveis necessárias (Tolerancia, )
    tol = 0,6
    fim = 0
    
#separa o texto em palavras
    texto = texto.split()
    
#Conta quantas palavras tem o texto
    tam = len(texto)
    
#Faz um loop dentro da database
    for i in range(len(FROM)):
        
#Avalia CADA elemento da database (From) e conta quantas palavras de cada elemento estão dentro do texto
        n = 0
        txt_from = FROM[i].split()
        for j in txt_from:
            if j in texto:
                n += 1
        
#Cria um quociente de quantas palavras de cada elemento são iguais as palavras do texto (Palavras iguais / numero de palavras de cada texto)
        quo = n/tam
        
#Se o quociente for maior ou igual à tolerância, retorna o elemento da database (To) correspondente ao match que deu no From
        if quo >= tol:
            return TO[i]
            fim = 1

#Se não encontrou nada, retorna variável vazia
    if fim == 0:
        return None

