class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    
    def __str__(self):
        return f'Nome : {self.nome} | Preço R$: {self.preco}'

class Estoque:
    def __init__(self):
        self.estoque=[]
        self.carrinho=[]
    
    def adicionar_carinho(self,produto):
        if  produto in self.estoque:
            print(f'{produto} adicinado com sucesso ao carrinho!')
            self.carrinho.append(produto)
        else:
            return f'{produto} não encontrado !'
        
    def remover_carinho(self,produto):
        if produto in self.carrinho:
            self.carrinho.remove(produto)
            print(f'{produto} removido do carrinho!')
        else:
            print(f'{produto} não está no carrinho!')

    def itens_no_carirnho(self):
        if self.carrinho:
            for item in self.carrinho:
                print(item)
        else:
            print('O carrinho esta vazio.')
            
    def adicionar_produto(self,produto):
        self.estoque.append(produto)
        
    def remover_estoque(self,produto):
        if produto in self.estoque:
            self.estoque.remove(produto)
            print(F'{Produto} removido do estoque!')
        else:
            print(f'{produto} não está no estoque!')
            
    def mostrar_estoque(self):
        for p, produto in enumerate(self.estoque,start=1):
            print(f'{p}.{produto}')
    
estoque=Estoque()        
produtos = [
        Produto('Mouse       ', 100),
        Produto('Teclado     ', 200),
        Produto('Celular     ', 1250),
        Produto('Tablet      ', 3260),
        Produto('Nootebok    ', 7540),
        Produto('Computador  ', 8960)
    ]
for produto  in produtos:
    estoque.adicionar_produto(produto)
    
print('Bem vindo a Loja!')
print('Aqui esta a lista de produtos em nosso estoque')

while True:
    while True:
        
        estoque.mostrar_estoque()
        print(f'"Digite sair para finalizar"')
        escolha=input('Digite o numero do item que você deseja adicionar ao carinho : ')
            
        if escolha.lower() == 'sair':
            break
        try:    
            escolha_num=int(escolha)
            if 1 <= escolha_num <=len(produtos):
                estoque.adicionar_carinho(estoque.estoque[escolha_num-1])
        
            else:
                print(f'Escolha invalida,por favor tente novamente!')
        except ValueError:
            print(f'Entrada invalida,por favor insira um número ou "sair"')
        
    while True:
        print(f'Certo aqui esta os itens no seu carrinho:')
        estoque.itens_no_carirnho()
        resp=input('Gostaria de remover algum item do carrinho?[S/N]')
        if resp.lower() == 'n':
            break
        elif resp.lower() == 's':
            nome_produto=input('Certo digite o nome do item que deseja remover:')
            produto_para_remover=None
            for produto in estoque.carrinho:
                produto_para_remover= produto
                break
            if produto_para_remover:
                estoque.remover_carinho(produto_para_remover)
            else:
                print(f'{nome_produto} não encontrado no carrinho')
    perg=input('Deseja continuar comprando?[S/N]')
    if perg.lower() in 'Nn':
        break
    
        
