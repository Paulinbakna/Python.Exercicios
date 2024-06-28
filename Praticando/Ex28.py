class Hotel:
    def __init__(self,numero_quarto,preco):
        self.numero_quarto=numero_quarto
        self.preco=preco
    
    def __str__(self):
        return f'Numero do quarto: {self.numero_quarto} | Preço R$: {self.preco}'

class Quarto:
    def __init__(self):
        self.quartos=[]
        self.quartos_reservados=[]
    def adicionar_quarto(self,quarto):
        self.quartos.append(quarto)
                
    def remover_quarto(self,quarto):
        if quarto in self.quartos:
            self.quartos.remove(quarto)
            print(f'Quarto N° removido  da lista de reservas')
        else:
            print(f'Quarto N°{quarto} não foi encontrado na lsita de reservas!')
        
    def reservar_quarto(self,quarto):
        if quarto in self.quartos:
            self.quartos.remove(quarto)
            self.quartos_reservados.append(quarto)
            print(f'Quarto N° {quarto} foi reservado!')
        else:
            print(f'O Quarto N° {quarto} não foi encontrado na lista de reservas!')
    def liberar_quarto(self,quarto):
        if quarto in self.quartos_reservados:
            self.quartos_reservados.remove(quarto)
            self.quartos.append(quarto)
            print(f'O Quarto N° {quarto} não está mais reservado!\n e foi adicionado a lsita de reservas!')
    
    def mostrar_quartos(self):
        for q,quarto in enumerate(self.quartos,start=1):
            print(f'{q}.{quarto}')
    
    
    def mostrar_reservados(self):
        for q,reservado in enumerate(self.quartos_reservados,start=1):
            print(f'{q}.{reservado}')
    
class Cliente:
    def __init__(self,nome,email):
        self.nome=nome
        self.email=email
    def __str__(self):
        return f'Nome: {self.nome} | Contato: {self.email}'
    
quarto=Quarto()

quartos = [
        Hotel('456',160),
        Hotel('854',160),
        Hotel('954',160),
        Hotel('524',160),
        Hotel('426',160)
    ]
for q in quartos:
    quarto.adicionar_quarto(q)
    
print('-'*40)
print('Bem Vindo ao Hotel Python')
print('-'*40)
nome=input('Antes de entrar digite seu nome:')
contato=input(f'Certo {nome} digite um email para contato: ')
cliente=Cliente(nome,contato)
print(f'Aq esta a lista de quartos disponiveis para reserva: ')
quarto.mostrar_quartos()
while True:
    while True:
        print("Digite sair para encerar o atendimento")
        escolha=input('Digite o numero  do quarto de deseja reservar:')
        if escolha.lower() == 'sair':
            break    

        escolha_num=int(escolha)
        if 1 <= escolha_num <= len(quartos):
            quarto.reservar_quarto(escolha[escolha_num-1])
    while True:
        quarto.mostrar_reservados()
        perg=input(f'Certo {nome} gostaria de remover algum quarto?[S/N]')
        if perg.lower() == 'n':
            break
        elif perg.lower() == 's':
            quarto_remover=input('Certo qual quarto deseja remover?')
            quarto_para_remover=None
            for quarto in quarto.quartos_reservados:
                quarto_para_remover=quarto
                break
            if quarto_para_remover:
                quarto.liberar_quarto(quarto_para_remover)
            else:
                print(f'Quarto não encontrado nos quartos reservados')
    print(cliente)
    quarto.mostrar_reservados()
    resp=input('Gostaria de reservar mais algum quarto?=[S/N]')
    if resp.lower() == 'n':
        break