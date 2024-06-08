class Empregado:
    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario
    
    def exibir_informacoes(self):
        print(f'Nome: {self.__nome}')
        print(f'Salario: {self.__salario}')
    
class Gerente(Empregado):
    def __init__(self, nome, salario,bonus_anual):
        super().__init__(nome, salario)
        self.__bonus_anual=bonus_anual
    
    def salario_total(self):
        return self._Empregado__salario + self.__bonus_anual
        
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Bonus Anual: {self.__bonus_anual}')
        print(f'Salario Total: {self.salario_total()}')
        
    
class Desenvolvedor(Empregado):
    def __init__(self, nome, salario,linguagem_programacao):
        super().__init__(nome, salario)
        self.__linguagem_programacao=linguagem_programacao
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Linguagem de Programação: {self.__linguagem_programacao}')
        

empregado=Empregado('João',1450)
empregado.exibir_informacoes()
print('---------------')
gerente=Gerente('Gabriel',1450,500)
gerente.exibir_informacoes()
print('---------------')
desenvolvedor=Desenvolvedor('Gustavo',4000,'Python')
desenvolvedor.exibir_informacoes()
print('---------------')
