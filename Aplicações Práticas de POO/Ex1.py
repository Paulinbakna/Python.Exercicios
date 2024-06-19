class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f'Nome: {self.nome}   |  Preço R$: {self.preco}'

class Cliente:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
    
    def __str__(self):
        return f'Nome do Cliente: {self.nome}\nContato: {self.contato}'

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.pagamento=0
        self.itens = []
    
    def adicionar_itens(self, item):
        self.itens.append(item)
    
    def remover_itens(self, item):
        self.itens.remove(item)
    
    def calcular_total(self):
        return sum(item.preco for item in self.itens)
    
    def mostrar_itens(self):
        for item in self.itens:
            print(f'Nome: {item.nome} | Preço R$ {item.preco}')
    def pagar(self):
        total=self.calcular_total()
        valor=self.pagamento
        
        if total < valor:
            conta=valor- total
            print(f'O cliente pagou a conta de R${self.calcular_total()} e ficou com R$ {conta} de troco')
        else:
            print(f'O Cliente não possui dinheiro suficiente para pagar a conta.')
            
    def __str__(self):
        itens_pedido = '\n'.join(str(item) for item in self.itens)
        total = self.calcular_total()
        return f'{self.cliente}\nItens do Pedido: \n{itens_pedido}\nTotal: R${total:.2f}'


print('-'*40)
mensagem='-- RESTAURANTE SIRI CASCUDO --'
mensagem.center(40)
print(mensagem)
print('-'*40)
print('Olá! Bem-vindo ao Siri Cascudo!')

# Get customer details
nome = input('Antes de entrar, por favor insira seu nome:\n-->> ')
contato = input('Certo, agora insira um email para contato:\n-->> ')
cliente = Cliente(nome, contato)
pedido = Pedido(cliente)

# Menu items
items = [
    Item('Coca-Cola', 6.00),
    Item('Vinho', 8.99),
    Item('Brownie', 4.99),
    Item('Salmão', 7.99),
    Item('Peixe Grelhado', 9.99)
]

# Main loop for ordering
while True:
    print('\nAqui está o cardápio do restaurante:')
    for i, item in enumerate(items, start=1):
        print(f'{i}. {item}')

    escolha = input('Digite o número do item que deseja pedir ou "sair" para finalizar:\n-->> ')

    if escolha.lower() == 'sair':
        break

    try:
        escolha_num = int(escolha)
        if 1 <= escolha_num <= len(items):
            pedido.adicionar_itens(items[escolha_num - 1])
            print(f'Item "{items[escolha_num - 1].nome}" adicionado ao pedido.')
        else:
            print('Escolha inválida, por favor tente novamente.')
    except ValueError:
        print('Entrada inválida, por favor insira um número ou "sair".')

    # Show final order
    print('\nPedido final:')
    print(pedido)
    carteira=input('Certo agora insira o valor que deseja pagar:\n-->> ')
    pedido.pagamento=carteira
    pedido.pagar()
    