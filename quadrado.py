#defina o tamanho do quadrado
#receba novo tamanho do lado do quadrado
#mude o tamanho do quadrado lateral do quadrado
#calcule a area do quadrado

class quadrado:
    def __init__(self, tamanho)-> None:
        self.tamanho= tamanho

    def mudar_tamanho(self):
        mudar= input("Troca o novo tamanho {}? [s/n]".format(self.tamanho)) 
        
        mudar = mudar[0].lower()

        if mudar == "s":
            novo_tamanho= input("\n> Novo Tamanho: ")
            self.tamanho= novo_tamanho
   
    def calcular_area(self.tamanho):
        return self.tamanho ** 2

    def main():
            
    