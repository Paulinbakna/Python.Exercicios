class Livro:
    def __init__(self,titulo,autor,numero_de_paginas):
        self.__titulo=titulo
        self.__autor=autor
        self.__numero_de_pagians=numero_de_paginas
    
    def exibir_informacoes(self):
        print(f'Titulo: {self.__titulo}')
        print(f'Autor: {self.__autor}')
        print(f'Numero de Paginas: {self.__numero_de_pagians}')
    
    def tempo_leitura(self):
        if self.__numero_de_pagians > 60:
            tempo=self.__numero_de_pagians/60
            print(f'Tempo estimado de leitura: {tempo:.2f} Horas')
        else:
            print(f'TEmpo estimado de leitura: {self.__numero_de_pagians} Minutos')
class LivroDigital(Livro):
    def __init__(self, titulo, autor, numero_de_paginas,tamanha_do_arquivo):
        super().__init__(titulo, autor, numero_de_paginas)
        self.__tamanho_do_arquivo=tamanha_do_arquivo
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Tamanho do arquivo: {self.__tamanho_do_arquivo} MB')
    

livro1=Livro('Python Basico','João Silva',100)
livro1.exibir_informacoes()
livro1.tempo_leitura()
print('------------------')
livro2=LivroDigital('Python Avançado','Maria Oliveira',200,100)
livro2.exibir_informacoes()
livro2.tempo_leitura()
print('------------------')
livro3=Livro('Python Iniciantes','Marcus Vinicius',60)
livro3.exibir_informacoes()
livro3.tempo_leitura()
print('------------------')
        