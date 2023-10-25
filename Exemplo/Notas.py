notas = [] 

#! negativa- não for
while True: 
    nota= float(input("notas (ou -1 para encerrar o programa): "))
    if nota != -1:
        notas.append(nota)
    else: 
        break
    
print(notas)
print("-----------")

for i in reversed(notas):
    print(i)
print("-----------")


print("soma Total: ", sum(notas))
media = sum(notas)/len(notas)
print("Media: ", media)
print("Tamanho: ", len(notas))

qtd=0
for maior in notas:
    if maior > media:
        qtd=qtd + 1
print("Qtda Maior que a Média: ", qtd)

print("-----------")

qtda=0
for menor in notas:
    if menor < 70:
        qtda= qtda + 1
print("Qtda Menor que 70: ", qtda)        

print("----Fim----")






