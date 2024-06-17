class Triangulo:
    def __init__(self,base,altura):
        self._base=base
        self._altura=altura
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self,valor):
        if valor <= 0:
            raise ValueError('Base não pode ser menor que zero!')
        self._base=valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self,valor):
        if valor <= 0:
            raise ValueError('Altura não pode ser menor que zero!')
        self._altura=valor
        
    @property
    def area(self):
        return f'Área do Triangulo: {(self._base*self._altura)/2}'

try:    
    triangulo=Triangulo(5,10)
    print('-'*15)
    print(triangulo.area)
    print('-'*15)
    triangulo.base = 15
    triangulo.altura = 10
    print(triangulo.area)
    print('-'*15)
    triangulo.base=-1
except ValueError as e:
    print(e)

