class Pessoa:
    def __init__(self,nome):
        self._nome=nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        if not valor:
            raise ValueError('O nome não pode ser vazio!')
        self._nome = valor
    
    @nome.deleter
    def nome(self):
        self._nome='...'
        
pessoa1=Pessoa('Junim')
print('-'*15)
print(f'Nome: {pessoa1.nome}')
print('-'*15)
pessoa1.nome= 'Clebin'
print(f'Nome: {pessoa1.nome}')
print('-'*15)
del pessoa1.nome
print(f'Nome: {pessoa1.nome}')
print('-'*15)

