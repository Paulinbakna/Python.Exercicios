class Veiculo:
    def __init__(self,marca,modelo,cor,ano):
        self.__marca=marca
        self.__modelo=modelo
        self.__cor=cor
        self.__ano=ano
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,value):
        if not value:
            raise ValueError('Marca não pode ser vazia')
        self.__marca= value
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,value):
        if not value:
            raise ValueError('Modelo não pode ser vazia')
        self.__modelo= value
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self,value):
        if not value:
            raise ValueError('Cor não pode ser vazio')
        self.__cor  = value
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,value):
        if not value:
            raise ValueError('Ano não pode ser vazio')
        self.__ano= value
    
try:
    carro=Veiculo('Ford','Mustang','Branco',2021)
    print(f'Marca: {carro.marca} \nModelo: {carro.modelo} \nCor: {carro.cor} \nAno: {carro.ano}')
except ValueError as e:
    print(e)

