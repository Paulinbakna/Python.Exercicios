class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
    def exibir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        
carro2=Carro('Ford','Mustang',2022)
carro2.exibir()
