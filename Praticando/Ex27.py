class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    
    def __str__(self):
        return f'Nome do produto: {self.nome} | Preço do Produto R$: {self.preco}'

class Estoque:
    def __init__(self):
        self.estoque=[]
        self.carrinho=[]
    
    def venda(self,produto):
        for produto in self.estoque:
            self.estoque.remove(produto)
            self.carrinho.append(produto)
            print(f'Produto adicinado com sucesso ao carrinho!')
        else:
            return f'{produto} não encontrado !'
        
    def remover_carinho(self,produto):
        self.carrinho.remove(produto)
        print(f'{produto} removido do carrinho!')
    
    def itens_no_carirnho(self):
        for item in self.carrinho:
            print(item)

    def mostrar_estoque(self):
        for produto in self.estoque:
            print(produto)
    
estoque=Estoque()        
produtos = [
        Produto('Mouse    ', 100),
        Produto('Teclado  ', 200),
        Produto('Celular  ', 1250),
        Produto('Tablet', 3260 ),
        Produto('Nootebok', 7540),
        Produto('Computador', 8960)
    ]
for produto  in produtos:
    estoque.adicionar_produto(produto)
print('Bem vindo a Loja!')
print('Aqui esta a lista de produtos em nosso estoque')

while True:
    try:
        estoque.mostrar_estoque()
        escolha=('Digite o numero do item que você deseja adicionar ao carinho')
        
        if escolha.lower() == 'sair':
            break
        
        escolha_num=int(escolha)
        if escolha_num < 0 or escolha_num  >= len(produtos):
            estoque.venda(produtos[escolha_num-1])
    
        else:
            print(f'Escolha invalida,por favor tente novamente!')
    except ValueError:
        print(f'Entrada invalida,por favor insira um número ou "sair"')
    while True:
        print(f'Certo aq esta os itens do carrinho:')
        estoque.itens_no_carirnho()
        resp=input('Gostaria de remover algum item do carrinho?[S/N]')
            
        
