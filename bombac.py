class bomba:
    def __init__(self, combustivel, valorg, quantidade) -> None:
        self.combustivel=combustivel
        self.valorg= valorg
        self.quantidade= quantidade
        pass

#função para calcular o valor total
    def calcular_valor(self):
        comb=input("qual o tipo?:  ") #estou pedindo o valor da quantidade
        self.combustivel=comb
       
        qtd= int(input("Quantos Litros?:  "))
        self.quantidade= qtd
        
        if comb=="gasolina":
           self.valorg= 5.50
           calcular_valor=float(self.valorg * self.quantidade)
       
        elif comb=="alcool":
            self.valorg= 1.00
            calcular_valor=float(self.valorg * self.quantidade)
        
        print("valor é: ", calcular_valor)
              
def main(): 
    
    bomb= bomba("gasolina", 5.50, 0)
    bomb.calcular_valor()
     
    
main()