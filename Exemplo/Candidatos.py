
Eleitores =int(input("Quantidade de Eleitores: " ))
print ('O numero de eleitores é: ', Eleitores)

Lista = ["1", "2", "3"]
print('Lista: ', Lista)

qtd1 = 0
qtd2 = 0
qtd3 = 0

for i in range(Eleitores):
    Vote=input("Escolha: ") 

    if Vote == Lista[0]:
        qtd1 += 1
    elif Vote == Lista[1]:
        qtd2 += 1
    elif Vote == Lista[2]:
        qtd3 += 1

print('Qtd1: ', qtd1)
print('Qtd2: ', qtd2)      
print('Qtd3: ', qtd3)      

if qtd1> qtd2 and qtd1>qtd3:
    print("\n Candidato 1 Vencedor \n")

if qtd3> qtd1 and qtd3>qtd2:
    print("\n Candidato 3 Vencedor \n")

if qtd2> qtd1 and qtd2>qtd3:
    print("\n Candidato  Vencedor \n")    


  


