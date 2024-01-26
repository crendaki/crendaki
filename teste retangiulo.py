class ponto:
    def __init__(self, x, y) ->None:
        self.x= x
        self.y= y
    
        
class retangulo:
    def __init__(self, ponto1 = 0, ponto2 = 0)->None:
        self.ponto1=ponto1
        self.ponto2=ponto2

    def ponto_central(self):    
        ponto1=float((self.ponto1.x1 + self.ponto1.x2)/2)
        ponto2=float((self.ponto2.y1 + self.ponto2.y2)/2)
        return(ponto1, ponto2)

def menu():
    
    def receber_eixos():
        eixos= input(" X1, X2, Y1 E Y2: ")
        primeiro= eixos.split()
        x1= float(primeiro[0])
        y1= float(primeiro[2])
        x2= float(primeiro[1])
        y2=float (primeiro[3])
        ponto1=(x1,y1)
        ponto1=(x2,y2)

  
    recebe=ponto(0,0)
    receber_eixos()
    retang=retangulo(0,0)
    retang.ponto_central()

menu()