class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self,autor=autor
        self.disponivel=True
    
    def emprestar(self):
        if self.disponivel == True:
            print(f'O livro: {self.titulo} esta disponivel para emprestimo!')
            return True
        else:
            print(f'O livro: {self.titulo} não esta disponivel para emprestimo!')
            return False
        
    def devolver(self):
        print(f'Devolvendo o Livro: {self.titulo}')
        self.disponivel = True