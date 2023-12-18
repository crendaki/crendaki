class ponto:
    def __init__(self, x, y) ->None:
        self.x= x
        self.y= y

    def receber_pontos(self):
        xi= int(input("Receber Xi: ", x))
        self.x= xi
        print("Novo ponto: ", xi)

def main():
    ponte= ponto(0, 0) 
    ponte.receber_pontos()

main()
