class ContaBancaria:
    def __init__(self,titular,saldo,numero_conta):
        self._titular=titular
        self._saldo= saldo
        self._numero_conta=numero_conta
    
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
            raise ValueError('O valor do deposito não pode ser negativo')
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
    
    def __repr__(self):
        return f'Nome do Titular: {self._titular}\nSaldo atual da conta R$: {self._saldo}\nNumero da conta: {self._numero_conta}'
try:
    conta=ContaBancaria('Maycon',150,135)
    print('-'*15)
    print(conta)
    print('-'*15)
    conta.depositar(50)
    print('-'*15)
    print(conta)
    print('-'*15)
    conta.sacar(25)
    print('-'*15)
    print(conta)
    print('-'*15)
    conta.sacar(200)
    print('-'*15)
    print(conta)
except ValueError as e:
    print(e)

