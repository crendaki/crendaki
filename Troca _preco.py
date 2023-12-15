class bomba:
    def __init__(self, combustivel, valorg, quantidade) -> None:
        self.combustivel=combustivel
        self.valorg= valorg
        self.quantidade= quantidade

    def trocar_preco(self):
                  
        mudar_preco=input("O preço do combustivel vai alterar {}?: [s/n]")
        mudar_preco = mudar_preco[0].lower()
            
        if mudar_preco =="s":
              novo_preco=float(input("Novo Preço: ")) 
              self.valorg=novo_preco    

        print("Novo preço é: ", novo_preco)             

def main():
    bomb= bomba("gasolina", 5.0, 100)   
    bomb.trocar_preco()  
    
main()
