class Veiculo:
    def __init__(self,marca,modelo):
        self.__marca=marca
        self.__modelo=modelo
    
    def exibir_informacoes(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo,numero_de_portas):
        super().__init__(marca, modelo)
        self.__numero_de_portas=numero_de_portas
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Numero de portas: {self.__numero_de_portas}')

class Motocicleta(Veiculo):
    def __init__(self, marca, modelo,modelo_guidao):
        super().__init__(marca, modelo)
        self.__modelo_guidao=modelo_guidao
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Modelo do guidão: {self.__modelo_guidao}')

carro=Carro('Ford','Mustang',4)
carro.exibir_informacoes()
print('-------------')

moto=Motocicleta('Honda','Biz','Esportivo')
moto.exibir_informacoes()
print('-------------')
