class bomba:
    def __init__(self, combustivel=("gasolina", "alcool"), valorg=5.50, valora=4.50, quantidade=0) -> None:
        self.valorg= valorg
        self.valora=valora
        self.quantidade= quantidade
        self.combustivel=("gasolina", "alcool")
        pass

#função para calcular o valor total
    def calcular_valor(self):
        comb=int(input("qual o tipo {}? :  ")) #estou pedindo o valor da quantidade
        self.combustivel=comb
        qtd= int(input("Quantos Litros {}?:  "))
        self.quantidade= qtd
        
        if comb=="gasolina"
            else
            calcular=float(self.valorg*self.quantidade)         
    

       
  
    
bomb = bomba(5.5, 0)
bomb.calcular_valor() 
    
