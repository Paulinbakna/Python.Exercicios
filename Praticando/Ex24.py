class Funcionario:
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario

class Gerente(Funcionario):
    def __init__(self, nome, salario,bonus):
        super().__init__(nome, salario)
        self.bonus=bonus
    
    def salario_total(self):
        return self.salario + self.bonus
        
    def __str__(self):
        return f'Nome do Gerente: {self.nome}\nSalario Sem Bonus: {self.salario}\nBonus: {self.bonus}\nSalario  Total: {self.salario_total()}'
    
    
class Assistente(Funcionario):
    def __init__(self, nome, salario,horas):
        super().__init__(nome, salario)
        self.horas=horas
    
    def bonus_horas(self):
        return self.horas * 66
    
    def __str__(self):
        return f'Nome do Assistente(a): {self.nome}\nSalario Sem Bonus: {self.salario}\nBonus: {self.bonus_horas()}\nSalario Total: {self.bonus_horas() + self.salario}' 
class Empresa:
    def __init__(self):
        self.funcionarios=[]
    
    def contratar_funcionario(self,funcionario):
        self.funcionarios.append(funcionario)
        print(f'O Funcionario {funcionario} foi contratado!')
        
    def demitir_funcionario(self,funcionario):
        self.funcionarios.remove(funcionario)
        print(f'O Funcionario {funcionario} foi demitido')
        
gerente1=Gerente('Marcos',2400,500)
gerente2=Gerente('Jonas',2400,500)
asistente1=Assistente('João',1500,10)
asistente2=Assistente('Clovis',1500,10)

empressa=Empresa()
empressa.contratar_funcionario(gerente1.nome)
print('-'*40)
print(gerente1)
print('-'*40)
empressa.contratar_funcionario(gerente2.nome)
print('-'*40)
print(gerente2)
print('-'*40)
empressa.contratar_funcionario(asistente1.nome)
print('-'*40)
print(asistente1)
print('-'*40)
empressa.contratar_funcionario(asistente2.nome)
print('-'*40)
print(asistente2)
print('-'*40)

empressa.demitir_funcionario(gerente2.nome)    
empressa.demitir_funcionario(asistente2.nome)
    