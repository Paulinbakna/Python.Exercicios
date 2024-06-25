class Produto:
    def __init__(self,nome,preco,desconto):
        self.nome=nome
        self.preco=preco
        self.desconto=desconto
    
    @property
    def preco_com_desconto(self):
        return self.preco * (1-self.desconto)

    def __str__(self):
        return f'Nome do produto: {self.nome}\nPreço do produto R$: {self.preco}\nDesconto: {self.desconto*100}%'

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco}, desconto={self.desconto*100}%)"
    
produto1=Produto('Teclado',34,0.1)
print(produto1)
print(f'Preço com desconto R$: {produto1.preco_com_desconto}')
