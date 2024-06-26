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
        if quarto in self.quartos:
            self.quartos.append(quarto)
            print(f'Quarto N° {quarto.numero_quarto} adicionado a lista de reservas!')
        else:
            print(f'Quarto N° {quarto} não foi encontrado na lista de reservas!')
        
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
        