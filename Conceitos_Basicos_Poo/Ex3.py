class ContaBancaria:
    def __init__(self,titular,numero_conta,saldo=0):
        self.titular=titular
        self.numero_conta=numero_conta
        self.saldo=saldo
    
    def depositar(self,valor):
        self.saldo +=valor
        print(f'Deposito no valor de R$ {valor:.2f} realizado com sucesso!')
        print(f'Saldo atual: R$ {self.saldo:.2f}')
    def sacar(self,valor):
        if self.saldo > valor:
            self.saldo -=valor
            print(f'Saque no valor de R$ {valor} realizado ocm sucesso!')
            print(f'Saldo atual: R$ {self.saldo}')
        else:
            print(f'Erro! Não e possivel realizar o saque no valor de R$ {valor}!')
            print(f'Erro apresentando: Saldo Insuficiente.')

cliente=ContaBancaria('Junim',12345,100)
cliente.depositar(100)
cliente.sacar(50)
cliente.sacar(50)
cliente.sacar(150)