class Animal:
    def __init__(self,nome):
        self.nome = nome
        
    def fazer_som(self):
        pass

    def imprimirNome(self):
        print(f'O nome do animal e : {self.nome}')
        
class Cachorro(Animal):
    def fazer_som(self):
        return 'Au Au'

class Gato(Animal):
    def fazer_som(self):
        return 'Miau Miau'

class Pardal(Animal):
    def fazer_som(self):
        return 'Piu Piu'

#cachorro= Cachorro('Clebin')
#gato= Gato('Junim')
#pardal=Pardal('Pardal')
#print(f'{cachorro.nome} faz: {cachorro.fazer_som()}')
#print(f'{gato.nome} faz: { gato.fazer_som()}')
#print(f'{pardal.nome} faz: {pardal.fazer_som()}')

#cachorro.imprimirNome()
#gato.imprimirNome()
#pardal.imprimirNome()

#------------------------------
def fazer_barulho(animal):
    print(f'{animal.nome} faz: {animal.fazer_som()}')

cachorro= Cachorro('Clebin')
gato= Gato('Junim')
pardal=Pardal('Pardal')

fazer_barulho(cachorro)
fazer_barulho(gato)
fazer_barulho(pardal)
