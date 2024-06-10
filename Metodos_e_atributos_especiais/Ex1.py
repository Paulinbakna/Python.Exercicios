class Veiculo:
    def __init__(self,marca,nome,cor,ano):
        self.nome=nome
        self.marca=marca
        self.cor=cor
        self.ano=ano

class Carro(Veiculo):
    def __init__(self,marca,nome,cor,ano):
        super().__init__(nome,marca,cor,ano)
    
    def __str__(self):
        return f'Nome do carro: {self.nome} \nMarca do carro: {self.marca} \nCor do carro:  {self.cor} \nAno do carro: {self.ano}'

class Moto(Veiculo):
    def __init__(self,nome,marca,cor,ano):
        super().__init__(nome,marca,cor,ano)
        
    def __str__(self):
        return f'Nome da Moto: {self.nome} \nMarca da Moto: {self.marca} \nCor da Moto:  {self.cor} \nAno da Moto: {self.ano}'

carro=Carro('Dodge','Ram','Vermelho',2024)
moto=Moto('Fam','Yamaha','Preto',2023)
print(carro)
print('='*40)
print(moto)
