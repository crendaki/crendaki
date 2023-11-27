def nome_escada(nome):
    for i in range (len(nome)):
        print(nome[:i+1])
       
  
def main():
    nome = input("Digite o seu nome: ")
    nome_escada(nome)
    
if __name__=="__main__":
    main()