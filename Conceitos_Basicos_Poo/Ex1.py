class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
    def exibir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        
carro1=Carro('Ford','Mustang',2021)
print(f'Marca: {carro1.marca}')
print(f'Modelo: {carro1.modelo}')
print(f'Ano: {carro1.ano}')
        