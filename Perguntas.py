lista = ('Telefonou para a vitima? '  , 'Esteve no local do crime? ', 'Mora perto da vitima? ', 
'Devia para a vitima? ', 'Já trabalhou com a vitima? ') 

qtdSim= 0

for i in lista:
    resposta = input (i)
    if resposta in ('Sim'):
       qtdSim +=1

if qtdSim < 2:
    print('\n Inocente \n')

elif qtdSim == 2:  
    print ('\n Suspeita \n')

elif qtdSim in (3, 4):
       print ('\n Cumplice \n')

elif qtdSim ==5:
    print ('\n Assassino \n')       