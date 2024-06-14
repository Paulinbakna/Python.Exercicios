class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,value):
        if not value:
            raise ValueError('Marca não pode ser vazio')
        self.__marca=value.strip()    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,value):
        if not value:
            raise ValueError('Modelo não pode ser vazio')
        self.__modelo=value.strip()
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,value):
        if  value <= 0:
            raise ValueError('Ano não pode ser um numero negativo')
        self.__ano=value
        
try:
    carro1=Carro('Ford','Mustang',2024)
    print(carro1)
    print('------------')
    carro2=Carro('Dodge','',2023)
    print(carro2)
except ValueError as e:
    print(e)
    
