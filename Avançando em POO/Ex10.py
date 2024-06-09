class Funcionario:
    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario
    
    def exibir(self):
        print(f'Nome: {self.__nome}')
        print(f'Salario R$ {self.__salario}')
    
    def salario_anual(self):
        total=self.__salario * 12
        print(f'Salario Anual R$ {total}')
class Professor(Funcionario):
    def __init__(self, nome, salario,disciplina):
        super().__init__(nome, salario)
        self.__disciplina=disciplina
    
    def exibir(self):
        super().exibir()
        print(f'Disciplina ensinada: {self.__disciplina}')
    
class Adiministrador(Funcionario):
    def __init__(self, nome, salario,departamento):
        super().__init__(nome, salario)
        self.__departamento= departamento
    
    def exibir(self):
        super().exibir()
        print(f'Departamento: {self.__departamento}')

professor=Professor('João',1450,'Ingles')
professor.exibir()
professor.salario_anual()
print('-----------------')
adiministrador=Adiministrador('Marcos',4500,'Tecnologia')
adiministrador.exibir()
adiministrador.salario_anual()
print('-----------------')
