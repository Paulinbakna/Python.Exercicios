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
        self.pagamento=0
    
    def adicionar(self,produto,quantidade):
        self.lista_produtos.append(produto)
        produto.quantidade=quantidade
        print(f'{produto} adicionado com sucesso a lista!')
    
    def remover(self,codigo):
        for produto in self.lista_produtos:
            if produto.codigo == codigo:
                self.lista_produtos.remove(produto)
                print(f'{produto} removido da lista')
                return
        print(f'Produto com o codigo: {codigo} não encontrado no sistema!')
        
        
    def atualizar_produto(self,codigo,nome=None,quantidade=None,preco=None):
        for produto in self.lista_produtos:
            if produto.codigo==codigo:
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
        total= sum(produto.preco * int(produto.quantidade)for produto in self.lista_produtos)
        return total
    
    def pagar(self):
        total=self.calcular()
        valor=self.pagamento
        
        if total <= valor:
            pedido=valor- total
            print(f'O cliente pagou o pedido de R${self.calcular():.2f} e ficou com R$ {pedido:.2f} de troco')
        else:
            print(f'O Cliente não possui dinheiro suficiente para pagar!.')
                    
    def __str__(self):
        produto_pedido = '\n'.join(str(produto) for produto in self.lista_produtos)
        total=self.calcular()
        return f'{self.fonecedor}\nItens do Pedido:\n {produto_pedido}\nTotal R$: {total:.2f}'
    

print('-'*40)
print('Bem Vindo ao Key Market')
print('-'*40)
try:
    nome=input('Ola Para começar insira seu nome:\n-->>')
    print('-'*40)
    contato=input(f'Certo {nome} agora insira um email para contato:\n-->>')
    print('-'*40)
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
    print('-'*40)   
except ValueError as e:
    print(e)
    
while True:
    while True:
        for i, produto in enumerate(produtos, start=1):
            print(f'{i}.{produto}')
        print('-'*40)   
        
        escolha=input('Digite o numero do item que deseja comprar ou "sair" para finalizar o pedido:\n-->>')
        
        if escolha.lower() == 'sair':
            break
        
        quantidade=input('Certo agora digite a quantidade:\n-->>')
        print('-'*40)   
        
        try:
            escolha_num = int(escolha)
            if 1 <= escolha_num <= len(produtos):
                estoque.adicionar(produtos[escolha_num - 1],quantidade)
                print('-'*40)    
            else:
                print(f'Escolha inválida, por favor tente novamente.')
        except ValueError:
            print(f'Entrada inválida, por favor insira um número ou "sair".')
            
    while True:
        try:
            print('-'*40)    
            print('\nPedido:')
            print(estoque)
            print('-'*40)
            carteira=float(input('Certo agora digite o valor para pagamento:\n-->>'))
            estoque.pagamento=carteira
            print('-'*40)
            estoque.pagar()
            break   
        except ValueError:
            print(f'Entrada inválida, por favor digite um valor numérico.')
    
    print('-'*40)
    continuar=input(f'Quer continuar?[S/N]\n-->>')
    
    if continuar in 'Nn':
        break

print('-'*40)
print(f'Até mais {nome} e volte sempre!')
    
        