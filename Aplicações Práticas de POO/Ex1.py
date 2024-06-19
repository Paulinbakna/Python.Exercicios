from colorama import Fore, Style
from time import sleep
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
        return f'Nome do Cliente: {self.nome}\nEmail para Contato: {self.contato}'

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
            print(f'{Fore.BLUE}Nome:{Style.RESET_ALL} {item.nome} | {Fore.LIGHTYELLOW_EX}Preço R$ {item.preco}')
    def pagar(self):
        total=self.calcular_total()
        valor=self.pagamento
        
        if total <= valor:
            conta=valor- total
            print(f'O cliente pagou a conta de R${self.calcular_total():.2f} e ficou com R$ {conta:.2f} de troco')
        else:
            print(f'O Cliente não possui dinheiro suficiente para pagar a conta.')
            
    def __str__(self):
        itens_pedido = '\n'.join(str(item) for item in self.itens)
        total = self.calcular_total()
        return f'{self.cliente}\nItens do Pedido: \n{itens_pedido}\n{Fore.LIGHTYELLOW_EX}Total: R${total:.2f}{Style.RESET_ALL}'


print('-'*40)
mensagem=f'{Fore.LIGHTRED_EX}-- RESTAURANTE SIRI CASCUDO --{Style.RESET_ALL}'
print(mensagem.center(40))
print('-'*40)
sleep(2)
print('Olá! Bem-vindo ao Siri Cascudo!')

# Get customer details
nome = input(f'Antes de entrar, por favor insira seu nome:\n{Fore.LIGHTGREEN_EX}-->> {Style.RESET_ALL}')
print('-'*40)
contato = input(f'Certo, {nome} agora insira um email para contato:\n{Fore.LIGHTGREEN_EX}-->>{Style.RESET_ALL} ')
print('-'*40)
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
print(f'Olá {nome} como você está?')
sleep(2)
print(f'{Fore.MAGENTA}Aqui está o cardápio do restaurante: {Style.RESET_ALL}')
while True:
    while True:
        print('-'*40)
        for i, item in enumerate(items, start=1):
            print(f'{i}. {item}')
        print('-'*40)

        escolha = input(f'Digite o número do item que deseja pedir ou "sair" para finalizar o pedido:\n{Fore.LIGHTGREEN_EX}-->>{Style.RESET_ALL} ')

        if escolha.lower() == 'sair':
            break
            
        try:
            escolha_num = int(escolha)
            if 1 <= escolha_num <= len(items):
                pedido.adicionar_itens(items[escolha_num - 1])
                print('-'*40)
                print(f'Item {Fore.LIGHTBLUE_EX} "{items[escolha_num - 1].nome}" {Style.RESET_ALL}adicionado ao pedido.')
                sleep(2)    
            else:
                print(f'{Fore.LIGHTRED_EX}Escolha inválida, por favor tente novamente.{Style.RESET_ALL}')
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}Entrada inválida, por favor insira um número ou "sair".{Style.RESET_ALL}')
    while True:
        try:
            sleep(2)    
            print('-'*40)
            print('\nPedido final:')
            print(pedido)
            print('-'*40)
            sleep(2)    
            carteira=float(input(f'Certo agora insira o valor que deseja pagar:\n{Fore.LIGHTGREEN_EX}-->> {Style.RESET_ALL}'))
            pedido.pagamento=carteira
            print('-'*40)
            pedido.pagar()
            break
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}Entrada inválida, por favor insira um valor numérico.{Style.RESET_ALL}')
                
    sleep(2)    
    print('-'*40)
    continuar=input(f'Quer continuar? [S/N]\n{Fore.LIGHTGREEN_EX}-->>{Style.RESET_ALL}').strip()[0]
    sleep(2)    
    if continuar in 'Nn':
        break

print('-'*40)
print(f'{Fore.LIGHTBLUE_EX}Até mais {nome} e volte sempre,Tenha um Bom Dia!{Style.RESET_ALL}')
