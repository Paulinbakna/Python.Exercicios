class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quatidade=quantidade
    
    def __str__(self):
        return f'Nome: {self.nome}\nPreço: R${self.preco}\nQuantidade em Estoque: {self.quatidade}'
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,value):
        if value < 0 :
            raise ValueError("Preço não pode ser negativo")
        self.__preco= value
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self,value):
        if value < 0:
            raise ValueError('A quantidade nao  pode ser negativa')
        self.__quantidade = value

try:        
    produto1=Produto('Teclado',99,100)
    print(produto1)
    print('-'*15)
    produto2=Produto('Teclado Mecanico',99,100)
    print(produto2)
    print('-'*15)
    produto3=Produto('Mouse',-1,100)
    print(produto3)
    print('-'*15)
    produto4=Produto('Mouse Pichau',25,-1)
    print(produto4)
    print('-'*15)
except ValueError as e:
    print(e)
    
