class Produto:
    def __init__(self,nome,preco):
        self.__nome=nome
        self.__preco= preco
    
    def exibir_informacoes(self):
        print(f'Nome: {self.__nome}')
        print(f'Preço: R$ {self.__preco}')

class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco,data_validade):
        super().__init__(nome, preco)
        self.__data_validade=data_validade
        
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Data de Validade: {self.__data_validade}')

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco,garantia):
        super().__init__(nome, preco)
        self.__garantia= garantia
        
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Garantia: {self.__garantia}')

produto_perecivel=ProdutoPerecivel('Leite',4.80,'10/06/2024')
produto_perecivel.exibir_informacoes()
print('------------')

produto_eletronico=ProdutoEletronico('Mouse',4.99,2)
produto_eletronico.exibir_informacoes()
