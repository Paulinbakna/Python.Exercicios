class Salario:
    def __init__(self,salario_base,bonus):
        self._salario_base=salario_base
        self._bonus=bonus
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self,valor):
        if valor <= 0:
            raise ValueError('O salário não pode ser negativo!')
        self._salario_base=valor
    
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self,valor):
        if valor <= 0 :
            raise ValueError('O bônus não pode ser negativo!')
        self._bonus=valor
    
    @property
    def salario_total(self):
        return f'Sálario base R$ {self._salario_base}\nBônus R$ {self._bonus}\nSálario Total R$ {self._salario_base+self._bonus}'

try:
    funcionario=Salario(1450,200)
    print(funcionario.salario_total)
    print('-'*15)
    funcionario.salario_base = 1000
    funcionario.bonus= 300
    print(funcionario.salario_total)
    print('-'*15)
    funcionario.salario_base= 1
    funcionario.bonus= -1
except ValueError as e:
    print(e)

    