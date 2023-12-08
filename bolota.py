#definir a classe bola
class bolota:
    def __init__(self, cor, circun, material) -> None:
        self.cor= cor
        self.circun= circun
        self.material= material  

    #função que pergunta se deseja trocar a cor   
    def troca_cor(self):
        troca= input("Deseja trocar a cor atual {}? [s/n]".format(self.cor)) 
#no caso da resposta ser S ou s ele troca por maiscula, pois é case sensitive
        troca = troca[0].lower()
#se desejar trocar a cor,  digite nova cor
        if troca == "s":
            nova_cor =input("\n> Nova Cor: ")
            self.cor= nova_cor
        else:   
            print("OK a cor continua {}".format(self.cor))     

    def mostra_cor(self):
        print("\nA cor atual é {}".format(self.cor))      

def main():
    bola01= bolota(cor="Azul", circun=5, material="metal")  

    while True:
        bola01.mostra_cor()
        bola01.troca_cor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola01.mostra_cor()

main()   