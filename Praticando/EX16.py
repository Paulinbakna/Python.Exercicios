class ContaBancaria:
    def __init__(self,saldo):
        self._saldo= saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor):
        if valor < 0:
            raise ValueError('O saldo não pode ser negativo')
        self._saldo == valor
    
    def depositar(self,valor):
        if valor < 0:
            raise ValueError('O valordo deposito não pode ser negativo')
        else:
            print(f'Deposito no valor de R$ {valor} realizado com sucesso!')
            self._saldo+=valor
    def sacar(self,valor):
        if valor < 0:
            raise ValueError('O Valor para saque não pode ser negativo!')
        if self._saldo - valor < 0:
            raise ValueError(f'Não e possivel realizar um saque no valor de R$ {valor}! Saldo Insuficiente!')
        else:
            print(f'Saque no valor de R$ {valor} realizado com sucesso!')
            self._saldo -=valor
        
try:
    conta=ContaBancaria(150)
    print('-'*15)
    print(f'Saldo atual  da conta: R${conta.saldo}')
    print('-'*15)
    conta.depositar(50)
    print('-'*15)
    conta.sacar(25)
    print('-'*15)
    conta.sacar(200)
except ValueError as e:
    print(e)

