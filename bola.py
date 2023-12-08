
#definido classe e atributos , __init__(metodo construtor) 'unknown' atributo desconhecido 

class Bola:
    def __init__(self, cor="unknown", material= "unknown", valor=0):
        self.cor = cor
        self.material = material        
        self.valor = valor

#imput para receber se deseja alterar a cor ou não
    def troca_cor(self):
        troca = input("Mudar a cor{}? [s/n]".format(self.cor))
    
        troca = troca[0].lower

        if troca=="S":
            nova_cor = input("\n> Nova Cor: ")
            self.cor = nova_cor   
        else:
            print ('Ok a cor continua{}'.format(self.cor))           
    def mostrar_cor(self):
        print("\nA cor atual é {}".format(self.cor))

def main():
    bola01 = Bola("Azul", "metal","1")
    bola01.troca_cor()
    bola01.mostrar_cor()   

main()       