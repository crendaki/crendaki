usado= {}
capacidade= 0


def calcular_total(): #espaço total utilizado
    usototal = sum(usado.values())/1024/1024
    return usototal  


def transforma():
    usado_individual = 0 #espaço utilizado individual
    contador = 0 #gera o indice do nome 

    for chave, valor in usado.items():  #para cada usuario e valor na lista 
       contador += 1 #fazer a numeração de indice de cada usuario
       usado_individual = float((valor)/1024/1024) #espaço utilizado individual pegue o valor e transforme em MB
       porcentagem = ((usado_individual/capacidade)*100) 
       r.write(f"\t{contador}\t\t{chave}:\t\t{usado_individual:9.2f} mb\t\t\t{porcentagem:>4.2f} % \n")   
#t = tabulação, f= formatação da string , tudo que estiver verde nessa linha é igual a formatação 

with open('usuario.txt', 'r') as f: #abertura do arquivo
       linhas = f.readlines()        #leitura individual das linhas do arquivo 
       for linha in linhas:          #para cada elemento individual da linha  
        #linha= os elementos individuais de cada linha (chave, espaço e valor) 
            (usuario, uso) = linha.split() #esplosão da linha
            usado[usuario] = float(uso)   #usado [usuario]= espaço utilizado por cada usuario = trazer o valor em numeros flutuantes
            f.close() #fechar o programa para não ter perigo de invasão


with open ('arquivo.txt', 'w+', encoding= 'utf8') as r: #leitura do arquivo
    r.write("ACM INC. \t\t\t\t Uso do Espaço em disco pelos usuarios\n \n") #formatação cabeçalho do arquivo
    r.write("-" * 80) #formatação dos tracinhos
    r.write("\n\n\n Nr. \t\t Usuário\t\t Espaço Utilizado \t % do uso\n\n") #cabeçalho do relatório para criar as colunas

    transforma()

    r.write("\n Total usado em disco: \t\t {:>2.2f} MB".format(capacidade)) #informação da capacidade total usada
    r.write("\n Média usada em disco:\t\t {:7.2f} MB".format(float(capacidade)/len(usado.values()))) #valor médio do espaço utilizado
    r.close()