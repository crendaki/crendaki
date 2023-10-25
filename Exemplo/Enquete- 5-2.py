votos = [] 
contador = 0

#receba a camisa
while True: 
    escolha = int(input("Informe a camisa entre 1 e 23: "))
    if escolha == 0:
        break
    if escolha > 23:
        print("\nopção invalida.Digite outro numero\n")
    else:
        votos.append(escolha)
        contador +=1
print("\n Quantidade de votos: ", len(votos),"\n")

print("\n Qual o melhor jogador? ")

QtdaVotosPorcamisa = {}

for escolha in votos:
    if escolha in QtdaVotosPorcamisa:
        QtdaVotosPorcamisa[escolha] +=1
    else:    
        QtdaVotosPorcamisa[escolha] =1

for escolha, quantidade in QtdaVotosPorcamisa.items():       
    print('O jogador com a camisa numero', escolha, 'recebeu: ', quantidade ) 