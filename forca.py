import random 
#função que escolhe aleatorio 


def print_forca(forca):
    print(' '.join(forca))
    print(" ")

palavras= ['banana', 'abacaxi', 'pepino','cebola','laranja']
#dicionario de palavras, criado por mim

palavra = random.choice(palavras)
       #escolha aleotoria da palavra pelo sistema, variavel que esta recebendo a palavra escolhida pelo sistema   
forca = ['_' for _ in range(len(palavra))]
#traz para a forca a palavra escolhida e transforma essa palavra em uma lista, percorre cada letra da palavra e busca a posição de cada letra
erros = 0
#contador de erros
ganhou= False

#enquanto a quantidade de erros for menor que 6, vai fazer um Loop pedindo para digitar letra
while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra: ')
    chute = str(input()).lower() # converte maiscula em minuscula

#se a letra não estiver dentro da palavra
    if chute not in palavra:
        erros +=1 #soma a quantidade de erros e guarda
        print(f'Você errou pela {erros}ª vez. Tente de novo!') #imprime a quantidade de erros
      
    else:
#metodo index= a psoição dentro de uma lista, para cada indice de letra 
         for index, letra in enumerate(palavra):
            if letra == chute:#se a letra for igual ao chute
                 forca[index]= chute #adicione a posição na forca
#se zerar os tracinhos
    if '_' not in forca:
        ganhou= True       #confirma que ganhou

    if ganhou:  #se ganhou
        print('Você ganhou! A Palavra era: ', palavra) #imprima a informação
    #caso contrario imprima perdeu e enforque
    else:
         print('Game Over! A palavra correta era:', palavra)
    print_forca(palavra)                 