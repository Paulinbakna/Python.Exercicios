class Retangulo:
    def __init__(self,largura,altura):
        self._largura=largura
        self._altura=altura
        
    def __str__(self):
        return f'Largura: {self.largura}\nAltura: {self.altura}'
    
    @property
    def largura(self):
        return self._largura
    
    @property
    def altura(self):
        return self._altura
    
    @property
    def area(self):
        return f'Area do Retangulo: {self._largura * self._altura}'
    
    @property
    def perimetro(self):
        return f'Perimetro do Retangulo: {2 * (self._largura * self._altura)}'

retangulo=Retangulo(5,2)
print(retangulo.area)
print(retangulo.perimetro)
