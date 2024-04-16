class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def exibir_informacoes(self):
        print("marca:", self.marca)
        print("modelo:",self.modelo)
        print("cor:", self.cor)
        print("ano:", self.ano)
        
carro1 = Carro("toyota", "Hilux", "prata", 2021)
carro2 = Carro("wolkswagen", "Amarok", 2022)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()