class Transporte:
    def __init__(self,tipo,capacidade):
        self.__tipo=tipo
        self.__capacidade=capacidade
    
    def exibir(self):
        print(f'Tipo: {self.__tipo}')
        print(f'Capacidade: {self.__capacidade} Litros')
    
class TansporteTerrestre(Transporte):
    def __init__(self, tipo, capacidade,tipo_combustivel):
        super().__init__(tipo, capacidade)
        self.__tipo_combustivel=tipo_combustivel
        
    def exibir(self):
        super().exibir()
        print(f'Tipo de combustivel: {self.__tipo_combustivel}')

class TransporteAereo(Transporte):
    def __init__(self, tipo, capacidade,altitude_maxima):
        super().__init__(tipo, capacidade)
        self.__atitude_maxima=altitude_maxima
    
    def exibir(self):
        super().exibir()
        print(f'Atitulde maxima: {self.__atitude_maxima} Metros')
    

carro=TansporteTerrestre('Mustang',50,'Etanol')
carro.exibir()
print('--------------')
aviao=TransporteAereo('Boing 777',1000,12000)
aviao.exibir()
print('--------------')
