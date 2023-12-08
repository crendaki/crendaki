import random 

def print_forca(forca):
    print(' '.join(forca))
    print(" ")

palavras= ['banana', 'abacaxi', 'pepino','cebola','laranja']

palavra = random.choice(palavras)
forca = ['_' for _ in range(len(palavra))]
erros = 0
ganhou= False

while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra: ')
    chute = str(input()).lower()

    if chute not in palavra:
        erros +=1 
        print(f'Você errou pela {erros}ª vez. Tente de novo!') 
        continue     
   
    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index]= chute 

    if '_' not in forca:
        ganhou= True     

if ganhou:  
        print('Você ganhou! A Palavra era: ', palavra ) 
    
else:
         print('Game Over! A palavra correta era:', palavra)
print_forca(palavra)                 