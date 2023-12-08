#defina o tamanho do quadrado
#receba novo tamanho do lado do quadrado
#mude o tamanho do quadrado lateral do quadrado
#calcule a area do quadrado

from pickle import TRUE


class quadrado:
    def __init__(self, tamanho)-> None:
        self.tamanho= tamanho

    def mudar_tamanho(self):
        mudar= input("Troca o novo tamanho {}? [s/n]".format(self.tamanho)) 
        mudar = mudar[0].lower()

        if mudar == "s":
            novo_tamanho= input("\nNovo Tamanho: ")
            self.tamanho= novo_tamanho
   
    def valor_tamanho(self):
        print("|nValor do lado é{} cm".format(self.tamanho))
    
    def calcular_area(self):
       print("\nA area do quadrado é {:2f} cm²".format(float(self.tamanho)*float(self.tamanho)))


def main():
    quadrado1=quadrado(input("Insira o valor de lado: "))

    while TRUE:
        quadrado1.mudar_tamanho()
        quadrado1.valor_tamanho()
        quadrado1.calcular_area() 

        continuar= input("\ncontinuar? [s/n]")
        continuar= continuar[0].lower()
        if continuar =="n":
            break
main()    
    