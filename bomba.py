class bomba:
    def __init__(self, tipo='gasolina', valor=0, quantidade=0) -> None:
        self.tipo= tipo
        self.valor= valor
        self.quantidade= quantidade
        pass

#função para calcular o valor total
    def calcular_valor(self):
        qntd=int(input("Qual a quantidade {}? :  ")) #estou pedindo o valor da quantidade
        self.quantidade = qntd #variavel local que esta armazenando a quanitdade
        valor_total = float(self.valor * self.quantidade) #calculo do valor  
        print(valor_total) #imprimi o valor
        return valor_total
    
bomb = bomba(5.5)
bomb.calcular_valor() 
    
