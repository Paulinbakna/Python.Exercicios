class Animal:
    def __init__(self,nome,especie):
        self.nome=nome
        self.especie=especie
    
    def __str__(self):
        return f'Nome do Animal: {self.nome} | Especie: {self.especie}'
    def emitir_som_gato(self):
        print(f'O {self.especie} {self.nome} emitiu um som ....Miau Miau....')
    
    def emitir_som_cachorro(self):
        print(f'O {self.especie} {self.nome} emitiu um som...Au Au...')
        
    def emitir_som(self):
        print(f'O {self.especie} {self.nome} emitiu um som...')
        
animal1=Animal('Cleiton','cachorro')
print(animal1)
animal1.emitir_som_cachorro()
animal2=Animal('Thor','Gato')
print(animal2)
animal2.emitir_som_gato()
animal3=Animal('Nemo','Peixe')
print(animal3)
animal3.emitir_som()
