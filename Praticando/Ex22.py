class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self._idade=idade
        
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,valor):
        if valor < 0:
            raise ValueError('Idade não pode ser menor que zero')
        self._idade=valor
        
    def __str__(self):
        return f'Nome: {self.nome} | idade: {self._idade}'
    
    def aniversario(self):
        self._idade+=1
        print(f'Parabêns {self.nome}!')

try:    
    pessoa1=Pessoa('João',22)
    print(pessoa1)
    pessoa1.aniversario()
    print(pessoa1)
    pessoa2=Pessoa('Junim',30)
    pessoa2.aniversario()
    pessoa2.idade=-5
    print(pessoa2)
except ValueError as e :
    print(e)
    