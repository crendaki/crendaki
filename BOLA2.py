class bolota:
    def __init__(self, cor, circun, material) -> None:
        self.cor= cor
        self.circum= circun
        self.material= material  
        pass

    def trocacor(self):
        troca= input("Deseja trocar a cor atual {}? [s/n]".format(self.cor))   