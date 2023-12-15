class bomba:
    def __init__(self, combustivel, valorg, quantidade) -> None:
        self.combustivel=combustivel
        self.valorg= valorg
        self.quantidade= quantidade

#função para calcular o valor total
    def calcular_valor(self):
        comb=input("qual o tipo do combustivel?:  ") #estou pedindo o valor da quantidade
        self.combustivel=comb
       
        qtd_litros= int(input("Quantos Litros para abastecer?:  "))
        
        if comb=="gasolina":
           self.valorg= 5.50
           calcular_valor=float(self.valorg * qtd_litros )

               
        if comb=="alcool":
            self.valorg= 3.00
            calcular_valor=float(self.valorg * self.quantidade)

            calcular_valor=float(self.valorg * qtd_litros )

             print("valor em R$ é: ", calcular_valor)


    def abastecer_por_valor(self):
        vlr_combus=int(input("qual o valor?: "))     
        
        if vlr_combus>= 0:
           calcular_combus=float(vlr_combus / self.valorg)
           calculo_litros = self.quantidade - calcular_combus 
           self.quantidade = calculo_litros
        
        print("Quantidade de Litros abastecidos é: ",calcular_combus ) 
        print("Quantidade de litros na bomba: ", self.quantidade)       



def main(): 
    
    bomb= bomba("gasolina", 5.0, 100)
    bomb.calcular_valor()  
    #bomb.abastecer_por_valor()  
    
main()