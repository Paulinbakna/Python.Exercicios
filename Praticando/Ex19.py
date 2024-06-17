class Livro:
    def __init__(self,titulo,autor):
        self._titulo=titulo
        self._autor=autor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self,valor):
        if not valor:
            raise ValueError('Titulo não pode ser vazio')
        self._titulo=valor
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self,valor):
        if not valor:
            raise ValueError('Autor não pode ser vazio')
        self._autor = valor
    
    @property
    def descricao(self):
        return f'Titulo do Livro: {self._titulo}\nAutor do Livro: {self._autor}'

try:
    manga=Livro('Dragon Ball','Akira')
    print(manga.descricao)
    print('-'*15)
    manga.titulo= 'One Piece'
    manga.autor= 'Oda'
    print(manga.descricao)
    print('-'*15)
    manga.titulo=''
except ValueError as e:
    print(e)
