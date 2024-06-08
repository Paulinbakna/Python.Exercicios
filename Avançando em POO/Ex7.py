class Reserva:
    def __init__(self,nome,numero_quarto):
        self.__nome=nome
        self.__numero_quarto=numero_quarto

    def exibir_informacoes(self):
        print(f'Nome do Hóspede: {self.__nome}')
        print(f'Numero do Quarto: {self.__numero_quarto}')
    
class Reversa_simples(Reserva):
    def __init__(self, nome, numero_quarto,duracao_estadia,preco_por_noite):
        super().__init__(nome, numero_quarto)
        self.__duracao_estadia=duracao_estadia
        self.__preco_por_noite=preco_por_noite
    
    def calcular_custo_total(self):
        return self.__duracao_estadia * self.__preco_por_noite
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Duração da estadia: {self.__duracao_estadia}')
        print(f'Custo Total: R${self.calcular_custo_total()}')
    
class Reserva_Luxo(Reserva):
    def __init__(self, nome, numero_quarto,servico_de_quarto,preco_por_noite):
        super().__init__(nome, numero_quarto)
        self.__servico_de_quarto=servico_de_quarto
        self.__preco_por_noite=preco_por_noite
        
    def calcular_custo_total(self,duracao_estadia):
        return duracao_estadia * self.__preco_por_noite + self.__servico_de_quarto
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Serviço de quarto incluido: R${self.__servico_de_quarto}')
    
reserva_simples=Reversa_simples('Joâo Silva',123,3,150)
reserva_simples.exibir_informacoes()
print('-----------------')
reserva_luxo=Reserva_Luxo('Maria Oliveira',202,50,300)
reserva_luxo.exibir_informacoes()
print(f'Custo total por 2 noites: R$ {reserva_luxo.calcular_custo_total(2)}')
print('-----------------')


