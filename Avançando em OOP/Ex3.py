class ContaBancaria:
    def __init__(self,numero_da_conta,saldo=0):
        self.__saldo=saldo
        self.__numero_da_conta= numero_da_conta
        
    def depositar(self,valor):
        if valor > 0:
            self.__saldo+=valor
            print(f'Deposito no valor de {valor} realizado com sucesso.')
        else:
            print('O valor do deposito tem que ser positivo')
            
    def sacar(self,valor):
        if 0 < valor <= self.__saldo:
            self.__saldo-=valor
            print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso')
        else:
            print(f'Nao foi possivel realizar o saque de R$ {valor}! Saldo Insuficiente.')
    def consultar_saldo(self):
        return self.__saldo
    
    def consultar_numero_da_conta(self):
        return self.__numero_da_conta
        
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_da_conta,saldo=0,limite_cheque_especial=0):
        super().__init__(numero_da_conta,saldo)
        self.__limite_cheque_especial=limite_cheque_especial
    
    def sacar(self,valor):
        soma=self.consultar_saldo() + self.__limite_cheque_especial
        if 0 < valor <=(soma):
            novo_saldo= self.consultar_saldo() - valor
            if novo_saldo < 0:
                self.limite_cheque_especial+=novo_saldo
            self._ContaBancaria__saldo=max(0,novo_saldo)
            print(f'Saque de R${valor} realizado com sucesso do cheque especial')
        else:
            print(f'Saldo  e limite de cheque especial insuficientes ou valor de saque invalido')
    
    def consultar_limite(self):
        return self.__limite_cheque_especial        

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_da_conta,saldo=0,taxa_de_juros=0.01):
        super().__init__(numero_da_conta,saldo)
        self.__taxa_de_juros=taxa_de_juros
        
    def aplicar_juros(self):
        juros=self.consultar_saldo() * self.__taxa_de_juros
        self.depositar(juros)
        print(f'Juros de R$ {juros} aplicado ao saldo.')
        
conta_corrente=ContaCorrente(numero_da_conta=123,saldo=100,limite_cheque_especial=250)
conta_corrente.depositar(50)
conta_corrente.sacar(50)
print(f'Saldo apos saque: R${conta_corrente.consultar_saldo():.2f}')
print(f'Limite cheque especial: R${conta_corrente.consultar_limite():.2f}')

conta_poupanca=ContaPoupanca(numero_da_conta=456,saldo=150,taxa_de_juros=0.05)
conta_poupanca.aplicar_juros()
print(f'Saldo apos aplicação do juros: R${conta_poupanca.consultar_saldo():.2f}')

try:
    print(conta_corrente.__saldo)
except AttributeError:
    print(f'Não e possivel acessar o atributo privado __saldo diretamente')
    
try:
    print(conta_poupanca.__taxa_de_juros)
except AttributeError:
    print(f'Não e possivel acessar o atributo privado __taxa_de_juros diretamente')