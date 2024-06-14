class Carro:
    def __init__(self,modelo,marca,ano,cor):
        self.__marca=marca
        self.__modelo=modelo
        self.__ano=ano
        self.__cor=cor
    #Ajusta para os parametros sejam mostrados corretamente 
    def __repr__(self):
        return f'Carro(marca= {self.__marca}\n,Modelo= {self.__modelo}\n,Ano= {self.__ano}\n,Cor= {self.__cor})'
    
    #Retorna uma mensagem formatada sem a necessidade de criar um print para isso
    def __str__(self):
        return f'Modelo: {self.__modelo}\nMarca: {self.__marca}\nAno: {self.__ano}\nCor: {self.__cor} '
    
    #verifica se um objeto e igual ao que for informado 
    def __eq__(self, value):
        if self.__marca == value.__marca:
            print(f'A marca do {self.__modelo} e igual a do {value.__modelo}')
        else:
            print(f'A marca do {self.__modelo} não e a mesma que a do {value.__modelo}')
        if self.__modelo == value.__modelo:
            print(f'O modelo do {self.__modelo} e igual o do {value.__modelo}')
        else:
            print(f'O modelo do {self.__modelo} não e o mesmo que o do {value.__modelo}')
        if self.__ano == value.__ano:
            print(f'O ano  do {self.__modelo} e igual a do {value.__modelo}')
        else:
            print(f'O ano  do {self.__modelo} não e o mesmo que o do {value.__modelo}')
        if self.__cor == value.__cor:
            print(f'A cor do  {self.__modelo} e igual a do {value.__modelo}')
        else:
            print(f'A cor do {self.__modelo} não e o mesmo que o do {value.__modelo}')
    #Verifica se um  valor e maior que o valor que for informado 
    def __lt__(self,value):
        if self.__ano < value.__ano:
            print(f'O Carro {self.__modelo} e mais velho que {value.__modelo}')
        else:
            print(f'O Carro {self.__modelo} e mais novo que {value.__modelo}')

carro1=Carro('Mustang','Ford',2023,'Vermelho')
carro2=Carro('Dodge','Ram',2024,'Branco')
carro3=Carro('Mustang','Ford',2024,'Vermelho')
print(carro1)
print('-'*10)
print(carro2)
print('-'*10)
print(carro3)
print('-'*10)
print(carro1 == carro3)
print('-'*10)
print(carro1 == carro2)
print('-'*10)
print(carro1 < carro2)
