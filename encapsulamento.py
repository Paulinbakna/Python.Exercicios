class Pet:
    def __init__(self,nome,peso):
        self.nome= nome
        self.peso=peso
    
    def imprimirPet(self):
        print(f'Nome do Pet: {self.nome}')
        print(f'Peso do  Pet: {self.peso}')
    
    def alimentarPet(self,comida):
        self.peso+=comida
#---------------------------------------
class Abrigo:
    __catalogo= []
    
    def adicionarPet(self,pet):
        self.__catalogo.append(pet)
    
    def imprimirAbrigo(self):
        print(f'Pets no abrigo:')
        print('----------------')
        for pet in self.__catalogo:
            pet.imprimirPet()
            print('----------------')
#---------------------------------------

abrigo= Abrigo()
pet= Pet('Clebinho', 10)
abrigo.adicionarPet(pet)

pet= Pet('Junim', 15)
abrigo.adicionarPet(pet)
abrigo.imprimirAbrigo()

abrigo.catalogo= []
abrigo.imprimirAbrigo()
