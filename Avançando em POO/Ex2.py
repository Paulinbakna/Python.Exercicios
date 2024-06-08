class Veiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        
    def acelerar(self):
        pass
    def frear(self):
        pass
    
class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def acelerar(self):
        print(f'O Carro {self.marca} {self.modelo} esta acelerando')
    
    def frear(self):
        print(f'O Carro {self.marca} {self.modelo} esta freando')

class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def acelerar(self):
        print(f'A Moto {self.marca}{self.modelo} esta acelerando')
    
    def frear(self):
        print(f'A Moto {self.marca}{self.modelo} esta freando')

class Avião(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def acelerar(self):
        print(f'O Aviâo esta acelerando')
    
    def decolar(self):
        print(f'O Avião esta decolando')
    
    def frear(self):
        print(f'O Aviâo esta freando')

lista_veiculos=[Carro('Ford ','Mustang'),Moto('Honda','CB 1000 Black Edition'),Avião('Boeing','757')]

for item in lista_veiculos:
    
    item.acelerar()
    
    if isinstance(item,Avião):
        item.decolar()    
    
    item.frear()
    
    print('---')