class Produto:
    def __init__(self,nome,codigo,quantidade,preco):
        self.nome=nome
        self.codigo=codigo
        self.quantidade=quantidade
        self.preco=preco
    
    def __str__(self):
        return f'Nome: {self.nome}  | Preço R$: {self.preco}  |  Quantidade: {self.quantidade} | Codigo: {self.codigo}'

class Fornecedor:
    def __init__(self,nome,contato):
        self.nome=nome
        self.contato=contato
    def __str__(self):
        return f'Nome do Fornecedor: {self.nome}\nEmail para contato: {self.contato}'

class Estoque:
    def __init__(self,fornecedor):
        self.fonecedor=fornecedor
        self.lista_produtos=[]
    
    def adicionar(self,produto,quantidade):
        self.lista_produtos.append(produto)
        produto.quantidade=quantidade
        self.lista_produtos.append(produto.quantidade)
        print(f'{produto} adicionado com sucesso a lista!')
    
    def remover(self,produto):
        self.lista_produtos.append(produto)
        print(f'{produto} removido da lista')
    
    def atualizar_produto(self,codigo,nome=None,quantidade=None,preco=None):
        for produto in self.lista_produtos:
            if nome is not None:
                produto.nome=nome
                print('Nome do produto alterado!')
                
            if quantidade is not None:
                produto.quantidade=quantidade
                print('Quantidade do produto alterada com sucesso!')
            if preco is not None:
                produto.preco=preco  
                print('Preço do produto alterado com sucesso!')
                return
        print(f'Produto com o codigo: {codigo} não encontrado no sistema!')
        
    def calcular(self):
        return produto.preco * produto.quantidade 
    
    def __str__(self):
        produto_pedido = '\n'.join(str(produto) for produto in self.lista_produtos)
        total=self.calcular()
        return f'{self.fonecedor}\nItens do Pedido: {produto_pedido}\nTotal R$: {total}'
    

print('-'*40)
print('Bem Vindo ao Key Market')
print('-'*40)

nome=input('Ola Para começar insira seu nome:\n-->>')
contato=input(f'Certo {nome} agora insira um email para contato:\n-->>')
fornecedor=Fornecedor(nome,contato)
estoque=Estoque(fornecedor)
produtos = [
    Produto('Mouse    ', 123 , 100  , 5.99),
    Produto('Teclado  ', 124 ,  80  , 8.99),
    Produto('Monitor  ', 125 ,  50  , 9.99),
    Produto('Gabinete ', 126 ,  75  , 7.99),
    Produto('Mouse Pad', 127 , 100  , 3.99)
]

print(f'Ola {nome} aqui esta a lista de produtos que temos em nosso estoque')
while True:
    while True:
        for i, produto in enumerate(produtos, start=1):
            print(f'{i}.{produto}')
        
        escolha=input('Digite o numero do item que deseja comprar ou "sair" para finalizar o pedido:\n-->>')
        quantidade=input('Certo agora digite a quantidade:\n-->>')
        
        if escolha.lower() == 'sair':
            break
        
        try:
            escolha_num = int(escolha)
            if 1 <= escolha_num <= len(produtos):
                estoque.adicionar(produtos[escolha_num - 1],quantidade)
                print('-'*40)    
            else:
                print(f'Escolha inválida, por favor tente novamente.')
        except ValueError:
            print(f'Entrada inválida, por favor insira um número ou "sair".')
            
        print('\nPedido:')
        print(estoque)
        