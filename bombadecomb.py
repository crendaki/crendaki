class bomba:
    def __init__(self, combustivel, valorg, quantidade) -> None:
        self.combustivel=combustivel
        self.valorg= valorg
        self.quantidade= quantidade

#função para calcular o valor total
    def calcular_litros(self):
        comb=input("qual o tipo do combustivel?:  ") #estou pedindo o valor da quantidade
        self.combustivel=comb
       
        abastecer_por_valor = int(input("Qual o valor para abastecer?:  "))
        
        if comb=="gasolina":
           self.valorg= 5.00
      
           calcular_litros=float(abastecer_por_valor/self.valorg)
           calcular_saida_tanque= float(self.quantidade - calcular_litros)
           self.quantidade=calcular_saida_tanque
           print("A quantidade comprada foi: ", calcular_litros,"litros")
           print("A quantidade restante na Bomba é : ", calcular_saida_tanque)
              
        if comb=="alcool":
           self.valorg= 3.00
           calcular_litros=float(abastecer_por_valor/self.valorg)
           calcular_saida_tanque= float(self.quantidade - calcular_litros)
           self.quantidade=calcular_saida_tanque
           print("A quantidade comprada foi: ", calcular_litros,"litros")
           
           print("A quantidade restante na Bomba é: ", calcular_saida_tanque)


    def calcular_valor(self):
        comb=input("qual o tipo do combustivel?:  ") #estou pedindo o valor da quantidade
        self.combustivel=comb
       
        abastecer_por_litros = int(input("Quantos litros para abastecer?:  "))

        if comb=="gasolina":
           self.valorg= 1.00

           calcular_valor=float(abastecer_por_litros * self.valorg)
           calcular_saida_tanque= int(self.quantidade - abastecer_por_litros)
           self.quantidade= calcular_saida_tanque
           print("O valor a ser pago é: ", calcular_valor)
           print("A quantidade restante na Bomba é : ", calcular_saida_tanque)
              
        if comb=="alcool":
           self.valorg= 3.00

           calcular_valor=float(abastecer_por_litros * self.valorg)
           calcular_saida_tanque= int(self.quantidade - abastecer_por_litros)
           self.quantidade= calcular_saida_tanque
           print("O valor a ser pago é: ", calcular_valor)

           print("A quantidade restante na Bomba é : ", calcular_saida_tanque)

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
    bomb.calcular_litros()
    bomb.calcular_valor()  
    
     
main()