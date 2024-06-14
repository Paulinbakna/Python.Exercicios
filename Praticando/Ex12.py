class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Garagem(Carro):
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        if isinstance(carro,Carro):
            self.carros.append(carro)
            print(f'Carro {carro} adicionado com sucesso a garagem!')
        else:
            raise TypeError('Você so pode adicionar objetos do tipo Carro!')
        
    def remover_carro(self, carro):
        if carro in self.carros:
            self.carros.remove(carro)
            print(f'Carro {carro} removido com sucesso da garagem!')
        else:
            print(f'O Carro {carro} não esta na garagem.')
            
    def listar_carros(self):
        if not self.carros:
            print('A garagem está vazia!')
        else:
            print('-- Lista de Carros --')
            for carro in self.carros:
                print(carro)
            print('-'*15)       

carro1=Carro('Ford','Mustang',2024)
carro2=Carro('Dodge','Ram',2023)
carro3=Carro('Toyota','Hilux',2020)
garagem=Garagem()
print('-'*15)
garagem.adicionar_carro(carro1)
garagem.adicionar_carro(carro2)
garagem.adicionar_carro(carro3)
print('-'*15)
garagem.listar_carros()
garagem.remover_carro(carro3)
print('-'*15)
garagem.listar_carros()