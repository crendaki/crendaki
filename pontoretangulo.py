class ponto:
    def __init__(self, x, y) ->None:
        self.x= x
        self.y= y

    def receber_pontos(self):
        x1= int(input("Receber X1: ", ))
        self.x= x1
        print("Novo ponto: ", x1) 
        
        y1= int(input("Receber Y1: "))
        self.y= y1
        print("Receber: ", y1)

        x2= int(input("Receber X2: ", ))
        self.x= x2
        print("Novo ponto: ", x2) 
        
        y2= int(input("Receber Y2: "))
        self.y= y2
        print("Receber: ", y2)

class retangulo:
    def __init__(self, canto1, canto2)->None:
       self.canto1=canto1
       self.canto2=canto2
      
    def calcular_centro (self):
        x_centro = float(self.canto1.x)/2 + float(self.canto2.x)/2 
        y_centro= float(self.canto1.y)/2 + float(self.canto2.y)/2
        return Ponto(x_centro, y_centro)



def main():
    ponte= ponto(0, 0) 
    ponte.receber_pontos()
    retang= retangulo(0,0) 
    canto1=ponto(x1, y1)
    canto2= ponto(x2, y2)
    retang.calcular_centro()


main()    