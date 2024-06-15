class Livro:
    def __init__(self,nome,autor,numero_paginas):
        self.nome=nome
        self.autor=autor
        self.numero_paginas=numero_paginas
    
    def __str__(self):
        return f'Nome do Livro: {self.nome}\nAutor do Livro: {self.autor}\nNumeros de Paginas: {self.numero_paginas}'
    
    def __lt__(self,value):
        if self.numero_paginas < value.numero_paginas:
            print(f'O livro {value.nome} tem mais paginas que o Livro {self.nome}')
            
    def __gt__(self,value):
        if self.numero_paginas > value.numero_paginas:
            print(f'O Livro {self.nome} tem mais paginas que o  Livro {value.nome}')
        return '---------------------------------------------'
    
    def __eq__(self, value):
        if self.nome == value.nome:
            print(f'Os Livros: {self.nome} e {value.nome} não tem o mesmo nome')
        else:
            print(f'Os livros:  {self.nome} e {value.nome} não possuem o mesmo nome')
            
        if self.autor == value.autor:
            print(f'Os livros:  {self.nome} e {value.nome} tem o mesmo autor')
        else:
            print(f'Os livros:  {self.nome} e {value.nome} não possuem o mesmo autor')
            
        if self.numero_paginas == value.numero_paginas:
            print(f'Os livros:  {self.nome} e {value.nome} tem a mesma quantidade de paginas')
        else:
            print(f'Os livros:  {self.nome} e {value.nome} não tem o mesmo numero de paginas')
        return '---------------------------------------------'
    
livro1=Livro('One Piece','Oda',3568)
livro2=Livro('Black Clover','Asta',1200)
livro3=Livro('Dragon  Ball','Akira',3500)
livro4=Livro('One Piece Gold','Oda',3500)
print(livro1 < livro2)
print(livro1 < livro3)
print(livro1==livro2)
print(livro1==livro3)
print(livro1==livro4)
